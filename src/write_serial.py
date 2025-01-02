import json
import os
import time

import serial
from dotenv import load_dotenv

from airflow_sensor import airflow_meter

load_dotenv()

port = os.getenv("PORT")
baudrate = os.getenv("BAUDRATE")


def write_to_serial(port: str, baudrate: int) -> None:
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
    write_to_serial(port=port, baudrate=baudrate)
