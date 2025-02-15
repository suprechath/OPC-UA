import sys
# sys.path.insert(0, "..")
import time
import random
from opcua import ua, Server

if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our objects
    machine1 = objects.add_object(idx, "Machine1")
    machine2 = objects.add_object(idx, "Machine2")

    # Add variables to Machine1 and writable
    m1_temp = machine1.add_variable(idx, "Temperature", 25.0)
    m1_pressure = machine1.add_variable(idx, "Pressure", 101.3)
    m1_speed = machine1.add_variable(idx, "Speed", 1500)
    m1_temp.set_writable()
    m1_pressure.set_writable()
    m1_speed.set_writable()
    print(f"{machine1},{m1_temp},{m1_pressure},{m1_speed}")

    # Add variables to Machine2 and writable
    m2_temp = machine2.add_variable(idx, "Temperature", 30.0)
    m2_pressure = machine2.add_variable(idx, "Pressure", 95.0)
    m2_speed = machine2.add_variable(idx, "Speed", 1600)
    m2_temp.set_writable()
    m2_pressure.set_writable()
    m2_speed.set_writable()
    print(f"{machine2},{m2_temp},{m2_pressure},{m2_speed}")

    
    # starting server
    server.start()
    print("OPC-UA Server started at ", uri)
    
    try:
        while True:
            # Simulating sensor data updates
            m1_temp.set_value(round(random.uniform(20, 30), 2))
            m1_pressure.set_value(round(random.uniform(95, 105), 1))
            m1_speed.set_value(random.randint(1400, 1600))

            m2_temp.set_value(round(random.uniform(25, 35), 2))
            m2_pressure.set_value(round(random.uniform(90, 100), 1))
            m2_speed.set_value(random.randint(1500, 1700))

            # print(f"Updated Machine1 -> Temp: {m1_temp.get_value()}°C, Pressure: {m1_pressure.get_value()} kPa, Speed: {m1_speed.get_value()} RPM")
            # print(f"Updated Machine2 -> Temp: {m2_temp.get_value()}°C, Pressure: {m2_pressure.get_value()} kPa, Speed: {m2_speed.get_value()} RPM")
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop()
        print("\nShutting down server...")