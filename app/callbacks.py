""" Callback functions for MQTT """
import logging
import os
import json

from paho.mqtt.client import Client

from app.data_processors import process_received_data

logger = logging.getLogger(__name__)


def on_connect(client: Client, *_) -> None:
    """
    The callback to subscribe into a topic for when the client receives
    a CONNACK response from the server.

    Args:
        client: MQTT client object
    """
    topic = os.environ["MQTT_TOPIC"]
    client.subscribe(topic)
    logger.info(f"Subscribed to the topic {topic}")


def on_subscribe(*_) -> None:
    """
    The callback for when the broker has has acknowledged the subscription.
    """
    logger.info("The broker has acknowledged the subscription")


def on_message(client: Client, userdata, message) -> None:
    """
    The callback for when a PUBLISH message is received from the broker.

    Args:
        client: MQTT client object
    """
    message = message.payload.decode("utf-8")
    logger.info(f"Received message: {message}")

    processed_message = process_received_data(json.loads(message))
    logger.info(f"Processed message: {processed_message}")
