import argparse
import os

import uvicorn
import yaml
from fastapi import FastAPI
from starlette_prometheus import PrometheusMiddleware, metrics

from src.common import logger
from src.services.service import ServiceHandler


def parse_args(args=None):
    parser = argparse.ArgumentParser(description="sample-ai-chat-app")
    parser.add_argument(
        "-c",
        "--config",
        # required=True,
        type=argparse.FileType("r"),
        default=os.getenv("config", ""),
        help="config file for %(prog)s",
    )
    return parser.parse_args(args)


config = yaml.load(parse_args().config.read(), Loader=yaml.SafeLoader)
service_handler = ServiceHandler(config, logger.AppLogger(config["logging"]))
app = FastAPI(
    docs_url=config["api_path_swagger"],
    title=config["api_title"],
    version=config["api_version"],
)
app.add_middleware(PrometheusMiddleware)
app.include_router(service_handler.router)
uvicorn.run(app, host=config["api_run_host"], port=config["api_run_port"])
