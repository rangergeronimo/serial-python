import json
import time

import serial

from airflow_sensor import airflow_meter


def write_to_serial(port: str = "/dev/ttyUSB0", baudrate: int = 9600) -> None:
    with serial.Serial(port=port, baudrate=baudrate) as ser:
        try:
            while True:
                data = airflow_meter()
                data_to_json = json.dumps(data)
                ser.write(data_to_json.encode())
                print(data_to_json)

                # Introduce a slight delay to simulate real-time readings
                time.sleep(5)

        except KeyboardInterrupt:
            print("Exiting...")


# Example usage
# sudo chmod 666 /dev/tty*
if __name__ == "__main__":
    write_to_serial()
