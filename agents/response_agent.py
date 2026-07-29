"""
agents/response_agent.py

Takes retrieved policy chunks + the student's question and generates
a clear, student-friendly answer using Google Gemini (free tier),
citing the source document.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from agents.message import AgentMessage

SYSTEM_PROMPT = """You are the Horizon Academic AI Assistant, a helpful assistant for \
Horizon Campus students. Answer questions ONLY using the provided policy context below. \

Rules:
- If the answer is not contained in the context, say you don't have that information \
  and suggest the student contact the Student Affairs Office.
- Be clear, concise, and student-friendly — avoid overly formal legal language.
- Always mention which policy document your answer is based on (e.g., "According to \
  the Attendance Policy...").
- Do not make up rules, numbers, or deadlines that are not in the context.
"""


class ResponseAgent:
    def __init__(self, model: str = "gemini-flash-latest", temperature: float = 0.2):
        self.llm = ChatGoogleGenerativeAI(model=model, temperature=temperature)

    def generate_answer(self, question: str, retrieved_chunks) -> str:
        context_blocks = []
        for doc, score in retrieved_chunks:
            source = doc.metadata.get("source", "Unknown source")
            context_blocks.append(f"[Source: {source}]\n{doc.page_content}")

        context_text = "\n\n---\n\n".join(context_blocks)

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=f"Policy Context:\n{context_text}\n\nStudent Question: {question}"
            ),
        ]

        response = self.llm.invoke(messages)

        # Gemini responses can come back as a string or as a list of content
        # blocks (e.g. [{"type": "text", "text": "...", "extras": {...}}]).
        # Normalize to plain text either way.
        content = response.content
        if isinstance(content, list):
            text_parts = []
            for block in content:
                if isinstance(block, dict) and "text" in block:
                    text_parts.append(block["text"])
                elif isinstance(block, str):
                    text_parts.append(block)
            return "\n".join(text_parts).strip()

        return content

    def receive_message(self, message: AgentMessage):
        """Receive a structured message from another agent and act on it."""
        if message.message_type != "context_found":
            raise ValueError(f"Unexpected message type: {message.message_type}")

        query = message.payload["query"]
        chunks = message.payload["chunks"]

        print(f"[response_agent] received message from {message.sender}: {message}")

        return self.generate_answer(query, chunks)