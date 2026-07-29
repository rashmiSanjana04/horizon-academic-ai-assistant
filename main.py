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
from agents.router_agent import RouterAgent


def main():
    print("=" * 60)
    print(" Horizon Academic AI Assistant")
    print(" Ask me about exam rules, late submissions, appeals, or attendance.")
    print(" Type 'exit' to quit.")
    print("=" * 60)

    retrieval_agent = RetrievalAgent(top_k=4)
    response_agent = ResponseAgent()
    router_agent = RouterAgent()

    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not question:
            continue
        category = router_agent.route(question)
        print(f"[router_agent] classified question as: {category}")
        
        message = retrieval_agent.send_message(question)
        answer = response_agent.receive_message(message)

        print(f"\nAssistant: {answer}")


if __name__ == "__main__":
    main()