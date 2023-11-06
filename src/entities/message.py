from datetime import datetime


class Message:
    def __init__(
        self,
        interaction_id: str,
        message_id: str,
        created_at: datetime,
        role: str,
        content: str,
        **kwargs
    ):
        self.interaction_id = interaction_id
        self.message_id = message_id
        self.content = content
        self.role = role
        self.created_at = created_at if created_at else datetime.utcnow()
        self.metadata = kwargs
