from typing import Optional

from src.entities.interaction import Interaction


class User:
    def __init__(
        self,
        user_id: str,
        interaction_list: Optional[list[Interaction]] = None,
    ):
        self.user_id = user_id
        self.interaction_list = interaction_list if interaction_list else list()

    def export_user_interactions(self):
        dict(
            id=self.user_id,
            interactions=[i.export_user_interactions() for i in self.interaction_list],
        )
