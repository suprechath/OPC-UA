import sys
from opcua import Client, ua
import time

#Define objects and variables in server
objects = ["Machine1", "Machine2"]
variables = ["Temperature", "Pressure","Speed"]

#Subscription for changing detection
class SubHandler:
    def __init__(self, node_map):
        self.node_map = node_map
    def datachange_notification(self, node, val, data):
        for(obj, var), mapped_node in self.node_map.items():
            if node == mapped_node:
                current_time = time.strftime("%H:%M:%S", time.localtime())
                print(f"{current_time}: {var} of {obj} = {val}")

if __name__ == "__main__":

    # connect to the created server -> server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")
    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    client.connect()
    print("Connected to OPC UA server")

    # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
    root = client.get_root_node()
    print("Server node#: ", root)

    # Detect value change in every 15sec
    node_map = {} 
    handler = SubHandler(node_map)
    sub = client.create_subscription(5000, handler)# Every 5sec

    # fetch NumericNodeId 
    for object_name in objects:
        for variable in variables:
            nodeID = root.get_child(["0:Objects", f"2:{object_name}", f"2:{variable}"])
            node_map[object_name,variable] = nodeID
            sub.subscribe_data_change(node_map[object_name,variable]) 
            match variable:
                case "Temperature":
                    print(f"{variable} of {object_name} = {nodeID.get_value()} °C")
                case "Pressure":
                    print(f"{variable} of {object_name} = {nodeID.get_value()} kPa")
                case "Speed":
                    print(f"{variable} of {object_name} = {nodeID.get_value()} RPM")

    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        client.disconnect()
        print("\nClient disconnected.")