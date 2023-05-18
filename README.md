# 💡 IoT CarTelemetry to NeuTrafix SMS Notification Script

This script connects to an MQTT broker, subscribes to the "CarTelemetry" topic, and sends an SMS message containing the received telemetry data using the NeuTrafix SMS API.

## Use Case: IoT Vehicle Monitoring and Alerting

This script enables real-time monitoring and alerting for IoT vehicle telemetry data. It connects to an MQTT broker and subscribes to the "CarTelemetry" topic to receive telemetry messages. Upon receiving a message, it extracts relevant information from the telemetry data, such as VIN, speed, fuel level, and location coordinates. The extracted data is then used to send an SMS notification using the NeuTrafix SMS API.


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


## Other Use Cases

- **IoT Telemetry Monitoring**:🌐 This script enables you to monitor telemetry data from IoT devices using MQTT and receive real-time SMS notifications. It can be used in applications such as remote asset monitoring, environmental sensing, and industrial control systems.

- **Alerts and Notifications **:⚠️ By subscribing to the "CarTelemetry" topic, you can use this script to trigger SMS notifications (Using NeuTrafix SMS API) based on specific telemetry events or thresholds. It allows you to receive immediate alerts for critical conditions or important updates. 

- **Fleet Management**:🚚 Integrating this script into a fleet management system allows you to gather vehicle telemetry data and send SMS notifications to fleet managers or drivers. It can help in monitoring vehicle performance, tracking maintenance schedules, and enhancing overall fleet efficiency.

- **Security Systems**:🔒 This script can be utilized in security systems where MQTT is used for communication between sensors, cameras, and control panels. By subscribing to MQTT topics related to security events, you can receive SMS alerts in real-time, enhancing the security and responsiveness of the system.

Feel free to customize and expand on these use cases to align with your specific application or domain.



## License

This script is licensed under the MIT License.





