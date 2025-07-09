import paho.mqtt.client as mqtt 

class AWSIoTCore:
    def __init__(self):
        self.mqtt_broker = "a2tesugpeh2cyq-ats.iot.eu-west-1.amazonaws.com"
        self.mqtt_port = 8883
        self.client_id = "iotconsole-26fb4ad4-62d4-4692-9f7c-7ae66f8c311f"

    def send_shutdown_command(self):
        command_topic = "lima_mantis/device/+/command"

        publish = mqtt.Client()