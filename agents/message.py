class AgentMessage:
    """A structured message passed between agents."""
    def __init__(self, sender, receiver, message_type, payload):
        self.sender = sender          # e.g. "retrieval_agent"
        self.receiver = receiver      # e.g. "response_agent"
        self.message_type = message_type  # e.g. "context_found"
        self.payload = payload        # the actual data (dict)

    def __repr__(self):
        return f"AgentMessage(from={self.sender}, to={self.receiver}, type={self.message_type})"