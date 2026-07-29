"""
agents/router_agent.py

Classifies a student's question into a policy category.
Uses Groq (Llama 3.1 8B) — a fast, low-cost model — because
classification is a simple sub-task that doesn't need deep reasoning.
"""

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

CATEGORIES = ["exam", "late_submission", "appeals", "attendance", "general"]

ROUTER_SYSTEM_PROMPT = f"""You are a question classifier for a university academic \
policy assistant. Classify the student's question into exactly ONE of these \
categories: {', '.join(CATEGORIES)}.

Reply with ONLY the category name, nothing else.
"""


class RouterAgent:
    """Routes incoming questions to a policy category using a fast Groq model."""

    def __init__(self, model: str = "llama-3.1-8b-instant"):
        self.llm = ChatGroq(model=model, temperature=0)

    def route(self, question: str) -> str:
        messages = [
            SystemMessage(content=ROUTER_SYSTEM_PROMPT),
            HumanMessage(content=question),
        ]
        result = self.llm.invoke(messages)

        category = result.content.strip().lower()

        if category not in CATEGORIES:
            return "general"
        return category