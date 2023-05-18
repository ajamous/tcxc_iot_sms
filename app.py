# TCXC IoT - MQTT Telemetry to NeuTrafix SMS  API Script
# Author: Ameed Jamous
# Company: TelecomsXChange.com

import paho.mqtt.client as mqtt
import subprocess
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("CarTelemetry")

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    print("Received message: " + payload)
    
    # Prepare SMS API request
    sms_api_request = {
        "smpp_account_config": {
            "system_id": "{username}",
            "password": "{password}"
        },
        "message": {
            "source_addr_npi": 0,
            "source_addr_ton": 5,
            "destination_addr_ton": 1,
            "destination_addr_npi": 1,
            "source_addr": "{Sender_ID}",
            "short_message": {
                "text": payload
            }
        },
        "destinations": [
            "{Destination_Numbers}"
        ]
    }
    
    # Convert the request to JSON
    sms_api_request_json = json.dumps(sms_api_request)
    
    # Invoke the NeuTrafix SMS API using curl
    curl_command = [
        'curl',
        '--location',
        'https://ntx-api.telin.net',
        '--header',
        'Content-Type: application/json',
        '--data',
        sms_api_request_json
    ]
    
    # Execute the curl command
    subprocess.run(curl_command, check=True)

# Create an MQTT client
client = mqtt.Client()

# Set username and password for TCXC IoT authentication
client.username_pw_set("{Iot_username}", "{iot_password}")

# Set the TCXC IoT mqtt broker address and port
client.connect("iot.telecomsxchange.com", 1888, 60)

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Start the MQTT client loop
client.loop_forever()
