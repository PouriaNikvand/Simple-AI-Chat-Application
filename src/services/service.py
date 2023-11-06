import logging
from datetime import datetime
from typing import Annotated, Any, Dict, Mapping

from fastapi import APIRouter, Body
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from starlette_prometheus import metrics

from src.adapters.mongo_adapter import (
    BaseMongoClient,
    InteractionsMongoClient,
    MessagesMongoClient,
)
from src.adapters.redis_adapter import InteractionsRedisClient
from src.common.utils import SingletonMixin
from src.entities.interaction import Interaction
from src.entities.message import Message
from src.entities.settings import Settings
from src.entities.user import User


class BaseService(SingletonMixin):
    mongo: BaseMongoClient
    config: Mapping
    logger: logging.Logger

    def __init__(self, config, logger) -> None:
        super().__init__()
        self.mongo: BaseMongoClient
        self.config = config
        self.logger = logger


class ServiceHandler(BaseService):
    def __init__(self, config, logger):
        super().__init__(config, logger)
        self.interactions_mongo_client = InteractionsMongoClient(
            **config["mongo"]["interactions"]
        )
        self.messages_mongo_client = MessagesMongoClient(**config["mongo"]["messages"])
        # self.redis_client = InteractionsRedisClient(**config["redis"]["interactions"])
        self.router = APIRouter()
        self.router.add_api_route("/metrics", metrics, methods=["GET"])
        self.router.add_api_route("/", self.redirect, methods=["GET"])
        self.router.add_api_route(
            "/get-interactions", self.get_interactions, methods=["POST"]
        )
        self.router.add_api_route(
            "/new-interactions", self.new_interactions, methods=["POST"]
        )
        self.router.add_api_route("/get-messages", self.get_messages, methods=["POST"])
        self.router.add_api_route("/new-message", self.new_messages, methods=["POST"])

    def redirect(self):
        RedirectResponse(self.config["api_path_swagger"])

    def get_user(self, user_id):
        user_doc = self.interactions_mongo_client.get_user_interactions(user_id)
        if user_doc:
            return User(**user_doc)
        return None

    def get_interactions(self, request: Dict[Any, Any]):
        interaction_list = self.interactions_mongo_client.get_user_interactions(
            request["user_id"]
        )
        if interaction_list:
            return [
                Interaction(**i).export_user_interactions() for i in interaction_list
            ]
        else:
            return {"id": "not found"}

    def new_interactions(self, request: Dict[Any, Any]):
        self.interactions_mongo_client.insert_one(
            {
                "user_id": request["user_id"],
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
                "settings": Settings(**request["settings"]).export_settings(),
                "message_list": list(),
            }
        )

    def get_messages(self, request: Dict[Any, Any]):
        messages_list = self.messages_mongo_client.get_messages(
            request["interaction_id"]
        )
        if messages_list:
            return [Message(**i).export_message() for i in messages_list]
        else:
            return {id: "not found"}

    def new_messages(self, request: Dict[Any, Any]):
        self.interactions_mongo_client.insert_one(
            {
                "interaction_id": request["interaction_id"],
                "content": request["content"],
                "created_at": request["created_at"],
                "role": request["role"],
            }
        )
