from opcua import Server
from datetime import datetime

# Create an OPC-UA server
server = Server()

# Set the endpoint (URL for clients to connect)
server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

# Setup a namespace (identifier for your data)
namespace = server.register_namespace("MyOPCUA_Server")

# Create an object node in the address space
myobj = server.nodes.objects.add_object(namespace, "MyObject")

# Add a variable node to the object
temperature = myobj.add_variable(namespace, "Temperature", 25.0)

# Set variable as writable
temperature.set_writable()

# Start the server
server.start()
print("OPC-UA Server started at opc.tcp://localhost:4840/freeopcua/server/")

try:
    while True:
        # Update the temperature value dynamically
        temperature.set_value(temperature.get_value() + 0.1)
except KeyboardInterrupt:
    print("\nShutting down server...")
    server.stop()
