import serial


def read_from_serial(port: str, baudrate: int) -> None:
    with serial.Serial(port, baudrate) as ser:
        try:
            while True:
                data = ser.readline().decode("utf-8").strip()
                print(f"Received: {data}")
        except serial.SerialException as e:
            print(f"Error: {e}")


# Example usage
# sudo chmod 666 /dev/tty*
if __name__ == "__main__":
    read_from_serial("/dev/ttyUSB1", 9600)  # Replace with your actual port and baudrate
