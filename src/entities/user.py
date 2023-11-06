from typing import Optional

from src.entities.interaction import Interaction


class User:
    def __init__(
        self,
        user_id: str,
        interaction_id_list: Optional[list[Interaction]] = None,
        **kwargs
    ):
        self.user_id = user_id
        self.interaction_id_list = (
            interaction_id_list if interaction_id_list else list()
        )
        self.metadata = kwargs
