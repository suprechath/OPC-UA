import sys
sys.path.insert(0, "..")
import time

from opcua import ua, Server

if __name__ == "__main__":

    # setup our server
    server = Server()
    # server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    # uri = "http://examples.freeopcua.github.io"
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()
    print("Object node number is ", objects)

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    print("My object node is ", myobj)
    myvar = myobj.add_variable(idx, "MyVariable", 0)
    print("My variable node is ", myvar)
    myvar.set_writable()    # Set MyVariable to be writable by clients

    # starting!
    server.start()
    print("OPC-UA Server started at ", uri)
    
    try:
        count = 0
        while True:
            time.sleep(10)
            count += 0.1
            myvar.set_value(count)

    # finally:
    except KeyboardInterrupt:
        #close connection, remove subcsriptions, etc
        server.stop()
        print("\nShutting down server...")