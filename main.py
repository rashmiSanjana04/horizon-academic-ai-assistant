"""
main.py

Entry point for the Horizon Academic AI Assistant (command-line version).

Usage:
    python main.py
"""

from dotenv import load_dotenv

load_dotenv()  # Load OPENAI_API_KEY from .env

from agents.retrieval_agent import RetrievalAgent
from agents.response_agent import ResponseAgent


def main():
    print("=" * 60)
    print(" Horizon Academic AI Assistant")
    print(" Ask me about exam rules, late submissions, appeals, or attendance.")
    print(" Type 'exit' to quit.")
    print("=" * 60)

    retrieval_agent = RetrievalAgent(top_k=4)
    response_agent = ResponseAgent()

    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not question:
            continue

        retrieved_chunks = retrieval_agent.retrieve(question)
        answer = response_agent.generate_answer(question, retrieved_chunks)

        print(f"\nAssistant: {answer}")


if __name__ == "__main__":
    main()