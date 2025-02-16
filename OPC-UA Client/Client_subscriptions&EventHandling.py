from opcua import Client
from opcua import ua

class SubHandler:
    def datachange_notification(self, node, val, data):
        print(f"Data changed: Node={node}, Value={val}")

server_url = "opc.tcp://localhost:4840/freeopcua/server/"
client = Client(server_url)
client.connect()

handler = SubHandler()
sub = client.create_subscription(500, handler)  # 500ms update rate
node = client.get_node("ns=2;i=2")  # Replace with your node ID
handle = sub.subscribe_data_change(node)

try:
    while True:
        pass  # Keep the script running to receive updates
except KeyboardInterrupt:
    client.disconnect()
