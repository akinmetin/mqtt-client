import logging
import os

from helpers import init_client

logging.basicConfig(level=os.environ["LOG_LEVEL"])


if __name__ == "__main__":
    client = init_client()
    client.connect(
        host=os.environ["MQTT_HOST"],
        port=int(os.environ["MQTT_PORT"]),
        keepalive=int(os.environ["CONN_KEEP_ALIVE"]))

    logger = logging.getLogger(__name__)
    client.enable_logger(logger)

    client.loop_forever()
