""" Helper functions for MQTT """
import os
import ssl

import paho.mqtt.client as mqtt

import callbacks


def _init_callbacks(client: mqtt.Client) -> None:
    """ Initializes callback handlers. """
    client.on_connect = callbacks.on_connect
    client.on_subscribe = callbacks.on_subscribe
    client.on_message = callbacks.on_message


def _get_client() -> mqtt.Client:
    """ Returns a MQTT client object. """
    client = mqtt.Client(clean_session=True, protocol=mqtt.MQTTv311)

    client.username_pw_set(
        os.environ["MQTT_USERNAME"],
        os.environ["MQTT_PASSWORD"])
    client.tls_set(
        ca_certs=os.environ["SSL_CERT_PATH"],
        cert_reqs=ssl.CERT_REQUIRED,
        tls_version=ssl.PROTOCOL_TLSv1_2)

    return client


def init_client() -> mqtt.Client:
    """ Initializes and returns a client with callbacks. """
    client = _get_client()
    _init_callbacks(client)
    return client
