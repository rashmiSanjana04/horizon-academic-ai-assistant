"""
agents/router_agent.py

A simple keyword-based router that classifies a student's question
into a policy category before retrieval happens.
"""


class RouterAgent:
    """Routes incoming questions to the correct policy category."""

    CATEGORIES = {
        "exam": ["exam", "invigilat", "misconduct", "cheat"],
        "late_submission": ["late", "submission", "deadline", "extension"],
        "appeals": ["appeal", "remark", "grade dispute", "review"],
        "attendance": ["attendance", "absent", "present"],
    }

    def route(self, question: str) -> str:
        """Return the best-matching category for the question, or 'general'."""
        question_lower = question.lower()

        for category, keywords in self.CATEGORIES.items():
            for keyword in keywords:
                if keyword in question_lower:
                    return category

        return "general"