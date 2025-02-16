import sys
sys.path.insert(0, "..")
from opcua import Client, ua
import time


if __name__ == "__main__":

    # connect to the created server -> server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")

    client.connect()
    print("Connected to OPC UA server")

    # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
    root = client.get_root_node()
    print("Server node#: ", root)

    # Node objects have methods to read and write node attributes as well as browse or populate address space
    print("Children of root are: ", root.get_children())

    m1_temp = root.get_child(["0:Objects","2:Machine1","2:Temperature"])
    m1_pressure = root.get_child(["0:Objects","2:Machine1","2:Pressure"])
    m1_speed = root.get_child(["0:Objects","2:Machine1","2:Speed"])
    m2_temp = root.get_child(["0:Objects","2:Machine2","2:Temperature"])
    m2_pressure = root.get_child(["0:Objects","2:Machine2","2:Pressure"])
    m2_speed = root.get_child(["0:Objects","2:Machine2","2:Speed"])

    try:
        while True:
            # Read value
            m1_temp_val = m1_temp.get_value()
            m1_pressure_val = m1_pressure.get_value()
            m1_speed_val = m1_speed.get_value()
            print(f"Machine1 -> \n  Temp: {m1_temp_val} °C\n  Pressure: {m1_pressure_val} kPa\n  Speed: {m1_speed_val} RPM")
            m2_temp_val = m2_temp.get_value()
            m2_pressure_val = m2_pressure.get_value()
            m2_speed_val = m2_speed.get_value()
            print(f"Machine2 -> \n  Temp: {m2_temp_val} °C\n  Pressure: {m2_pressure_val} kPa\n  Speed: {m2_speed_val} RPM")
            time.sleep(10)
    except KeyboardInterrupt:
        client.disconnect()
        print("\nClient disconnected.")