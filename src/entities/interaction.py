from datetime import datetime
from typing import List, Optional

from src.entities.message import Message
from src.entities.settings import Settings


class Interaction:
    """ "
    an intersection is an object that contains the messages in event order
    it also contains metadata of that intersection
    """

    def __init__(
        self,
        interaction_id: str,
        created_at: datetime,
        updated_at: datetime,
        settings: dict,
        message_list: Optional[List[Message]] = None,
    ):
        self.interaction_id = interaction_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.settings = Settings(**settings)
        self.message_list = message_list if message_list else list()

    def export_user_interactions(self):
        dict(
            id=self.interaction_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            settings=self.settings.export_settings(),
            messages=[i.export_message() for i in self.message_list],
        )
