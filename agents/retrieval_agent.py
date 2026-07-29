"""
agents/retrieval_agent.py

Responsible for searching the policy knowledge base and returning
the most relevant chunks for a given student question.
"""

from rag.pipeline import load_vector_store
from agents.message import AgentMessage


class RetrievalAgent:
    def __init__(self, top_k: int = 4):
        self.vector_store = load_vector_store()
        self.top_k = top_k

    def retrieve(self, query: str):
        """
        Search the vector store for chunks relevant to the query.
        Returns a list of (document, score) tuples.
        """
        results = self.vector_store.similarity_search_with_score(
            query, k=self.top_k
        )
        return results

    def send_message(self, query: str):
        """Retrieve chunks and wrap them in a structured message for another agent."""
        chunks = self.retrieve(query)
        return AgentMessage(
            sender="retrieval_agent",
            receiver="response_agent",
            message_type="context_found",
            payload={
                "query": query,
                "chunks": chunks
            }
        )