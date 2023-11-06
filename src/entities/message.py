from datetime import datetime


class Message:
    def __init__(
        self,
        interaction_id: str,
        message_id: str,
        created_at: datetime,
        role: str,
        content: str,
    ):
        self.interaction_id = interaction_id
        self.message_id = message_id
        self.content = content
        self.role = role
        self.created_at = created_at if created_at else datetime.utcnow()

    def export_message(self):
        return dict(
            id=self.message_id,
            content=self.content,
            role=self.role,
            created_at=self.created_at,
        )
