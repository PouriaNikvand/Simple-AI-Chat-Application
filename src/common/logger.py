import logging
from datetime import datetime
from logging import Logger

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

from src.common.utils import Singleton

name_to_level = logging.getLevelNamesMapping()


class AppLogger(Logger, metaclass=Singleton):
    def __init__(self, config=None):
        if not config:
            raise NotImplementedError

        sentry_logging = LoggingIntegration(
            level=logging.INFO, event_level=logging.WARNING
        )
        sentry_sdk.init(dsn=config["sentry_dsn"], integrations=[sentry_logging])  # type: ignore

        Logger.__init__(self, name=config["name"])

        config = config["handlers"]
        file_handler = logging.FileHandler(
            filename=f'{config["file_handler"]["parent_directory"]}'
            f'{config["file_handler"]["run_mode"]}-'
            f'{config["file_handler"]["invoked_from"]}-'
            f'{datetime.now().strftime("%Y-%m-%d-%H")}.log'
        )
        file_handler.setLevel(name_to_level[config["file_handler"]["level"]])
        formatter = logging.Formatter(
            config["file_handler"]["format"], datefmt=config["file_handler"]["datefmt"]
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
