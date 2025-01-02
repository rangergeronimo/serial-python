import random


def airflow_meter() -> dict[str:float, float]:
    while True:
        # Simulate pressure in mbar (millibar)
        pressure_mbar = random.uniform(980, 1030)  # Typical atmospheric pressure range

        # Simulate flow in ccm (cubic centimeters per minute)
        flow_ccm = random.uniform(0, 500)  # Adjust range based on expected flow values

        # Return readings
        # print(f"Pressure: {pressure_mbar:.2f} mbar | Flow: {flow_ccm:.2f} ccm")
        return {"Pressure": pressure_mbar, "Flow": flow_ccm}


if __name__ == "__main__":
    print(airflow_meter())
    print(type(airflow_meter()))
