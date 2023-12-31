import logging
import os
from datetime import datetime
from logging import Logger

import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

from src.common.utils import Singleton

name_to_level = logging.getLevelNamesMapping()


class AppLogger(Logger, metaclass=Singleton):
    def __init__(self, config=None):
        if not config:
            raise NotImplementedError

        sentry_sdk.init(dsn=config["sentry_dsn"], integrations=[FastApiIntegration("endpoint")])  # type: ignore

        Logger.__init__(self, name=config["name"])

        config = config["handlers"]
        os.makedirs(config["file_handler"]["directory"], exist_ok=True)
        file_handler = logging.FileHandler(
            filename=f'{config["file_handler"]["directory"]}'
            f'{config["file_handler"]["run_mode"]}-'
            f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'
        )
        file_handler.setLevel(name_to_level[config["file_handler"]["level"]])
        formatter = logging.Formatter(
            config["file_handler"]["format"],
            datefmt=config["file_handler"]["date_format"],
        )
        file_handler.setFormatter(formatter)
        self.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            config["stream_handler"]["format"],
            datefmt=config["stream_handler"]["date_format"],
        )
        console_handler.setFormatter(formatter)
        console_handler.setLevel(name_to_level[config["stream_handler"]["level"]])
        self.addHandler(console_handler)


def log(text: str, level: int = logging.INFO):
    logger = AppLogger()
    logger.log(level=level, msg=text)
