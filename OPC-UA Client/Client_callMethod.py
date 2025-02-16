obj = client.get_node("ns=2;i=2")  # Get object
method = obj.get_child(["0:MyMethod"])  # Get method
result = method.call(5, 10)  # Call method with arguments
print("Result:", result)
