import sys
# sys.path.insert(0, "..")
from opcua import Client, ua


if __name__ == "__main__":

    # connect to the created server -> server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    

    try:
        client.connect()
        print("Connected to OPC UA server")

        # uri = "http://examples.freeopcua.github.io"
        # idx = client.get_namespace_index(uri)
        # print(idx)

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Server node#: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children())

        # Now getting a variable node using its browse path
        # m1_temp = client.get_node(f"ns={idx};s=Machine1.Temperature")
        # m1_pressure = client.get_node(f"ns={idx};s=Machine1.Pressure")
        # m1_speed = client.get_node(f"ns={idx};s=Machine1.Speed")
        m1_temp = root.get_child(["0:Objects","2:Machine1","2:Temperature"])
        m1_pressure = root.get_child(["0:Objects","2:Machine1","2:Pressure"])
        m1_speed = root.get_child(["0:Objects","2:Machine1","2:Speed"])

        # myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
        # obj = root.get_child(["0:Objects", "2:MyObject"])
        # print("myvar is: ", myvar)
        # print("myobj is: ", obj)

        # Read value
        m1_temp_val = m1_temp.get_value()
        m1_pressure_val = m1_pressure.get_value()
        m1_speed_val = m1_speed.get_value()
        print(f"{m1_temp_val},{m1_pressure_val},{m1_speed_val}")

        # # Write a new value
        # myvar.set_value("Hello OPC UA")
        # print("New value written")

        # # Read again
        # updated_value = myvar.get_value()
        # print(f"Updated Value: {updated_value}")

    except KeyboardInterrupt:
        client.disconnect()
        print("\nClient disconnected.")