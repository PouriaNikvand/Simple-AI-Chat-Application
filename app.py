import argparse
import os
import yaml


def parse_args(args=None):
    parser = argparse.ArgumentParser(description="sample-ai-chat-app")
    parser.add_argument(
        "-c",
        "--config",
        # required=True, # commented to allow load from ENV
        type=argparse.FileType("r"),
        default=os.getenv("config", ""),
        help="config file for %(prog)s",
    )
    return parser.parse_args(args)


def start():
    pass


def main():
    config = yaml.load(parse_args().config.read(), Loader=yaml.SafeLoader)

    # TODO create and start the app
    start()


if __name__ == "__main__":
    main()
