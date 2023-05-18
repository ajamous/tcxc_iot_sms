# MQTT Telemetry to SMS Script

This script connects to an MQTT broker, subscribes to the "CarTelemetry" topic, and sends an SMS message containing the received telemetry data using the NeuTrafix SMS API.

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```
   
## Usage

Modify the script with your specific configurations:
Update the SMS API request parameters in the on_message function according to your SMS gateway provider's specifications.
Set the MQTT authentication credentials (Iot_username and iot_password) in the script.
Adjust the MQTT broker address and port if necessary.
Run the script using the following command:

```shell
python mqtt_telemetry_to_sms.py
```

The script will connect to the TCXC IoT MQTT broker, subscribe to the "CarTelemetry" topic, and start listening for incoming telemetry messages. Once a message is received, it will be sent as an SMS using the configured SMS API.

License

This script is licensed under the MIT License.

Author

Ameed Jamous
Company

TelecomsXChange.com



