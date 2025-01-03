import time

import serial


def read_from_bardcode(port: str) -> None:
    with serial.Serial(port, baudrate=9600, timeout=1) as ser:
        while True:
            data = ser.readline().decode("utf-8").strip()
            if data:
                print(f"Barcode scanned: {data}")
            time.sleep(1)


if __name__ == "__main__":
    port = "/dev/ttyUSB1"  # Replace '/dev/ttyUSB0' with the actual port if different
    read_from_bardcode(port)
