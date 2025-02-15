from opcua import Client

# Connect to the server
client = Client("opc.tcp://localhost:4840/freeopcua/server/")
client.connect()
print("Connected to OPC-UA Server")

# Get the root node
root = client.get_root_node()

# Print root information
print("Root node:", root)

# Access the temperature variable
temperature_node = root.get_child(["0:Objects", "2:MyObject", "2:Temperature"])

# Read value
print("Temperature:", temperature_node.get_value())

# Write new value
temperature_node.set_value(30.5)
print("Updated Temperature:", temperature_node.get_value())

# Disconnect
client.disconnect()
