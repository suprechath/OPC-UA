import sys
sys.path.insert(0, "..")
from opcua import Client, ua


if __name__ == "__main__":

    # connect to the created server -> server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()
        print("Connected to OPC UA server")

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        # print("Children of root are: ", root.get_children())

        # get a specific node knowing its node id
        # var = client.get_node(ua.NodeId(1002, 2))
        var = client.get_node("ns=2;i=2")
        print(var)
        print(var.get_data_value()) # get value of node as a DataValue object
        #var.get_value() # get value of node as a python builtin
        #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type

        # # Now getting a variable node using its browse path
        # myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
        # obj = root.get_child(["0:Objects", "2:MyObject"])
        # print("myvar is: ", myvar)
        # print("myobj is: ", obj)

        # # Read value
        # value = myvar.get_value()
        # print(f"Current Value: {value}")

        # # Write a new value
        # myvar.set_value("Hello OPC UA")
        # print("New value written")

        # # Read again
        # updated_value = myvar.get_value()
        # print(f"Updated Value: {updated_value}")

    except KeyboardInterrupt:
        client.disconnect()
        print("\nClient disconnected.")