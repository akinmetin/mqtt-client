# Instructions

Please follow these instructions to start the dev MQTT server:

1- Create a `venv` (`python -m venv venv`) and activate it (`source venv/bin/activate`) in the root folder of this project.

2- Install dependencies `pip install -r requirements-dev.txt`.

3- Set these necessary environment variables:

---

`MQTT_TOPIC`: Topic name

`MQTT_HOST`: Hostname/IP of the server

`MQTT_PORT`: Server port

`MQTT_USERNAME`: Server user

`MQTT_PASSWORD`: User password

`SSL_CERT_PATH`: CA certificate path

`CONN_KEEP_ALIVE`: Connection keep-alive seconds

`LOG_LEVEL`: Log level of the client

---

3- Start the server `python app/client.py`.

# Testing

Test cases can be found in the root `tests` folder.

1- Run `coverage run -m pytest tests` to run all test cases and generate coverage report.

2- Coverage report can be observed with `coverage report`.
