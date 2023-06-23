import pickle
import socket
from token_module import Token  # Assuming Token class is defined in a separate module

# Function to update the key of the Token object
def update_token_key(token):
    # Perform key update logic here
    token.update_key()  # Assuming 'update_key' is a method in the Token class

# TCP server code
TCP_IP = 'localhost'  # IP address of the server
TCP_PORT = 5005  # Port number

# Create a TCP socket
#server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
#server_socket.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections
#server_socket.listen(1)

#print("Waiting for a connection...")

# Accept a client connection
#client_socket, address = server_socket.accept()
#print("Connection established with:", address)

# Receive the serialized Token object
#serialized_token = client_socket.recv(4096)

# Deserialize the Token object using pickle
#received_token = pickle.loads(serialized_token)

# Call the update_token_key function on the received token
#update_token_key(received_token)

# Send the updated Token object to a different address
new_address = ('localhost', 5005)  # New address to send the updated Token
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
new_socket.connect(new_address)

# Serialize the updated Token object
test_token=Token()
test_token.calculate_and_save_sum_of_smallest_jaccard_distances("tensors.txt")
test_token.calculate_and_print_mean_vector("tensors.txt")
test_token.update_comments()
serialized_updated_token = pickle.dumps(test_token)

# Send the serialized updated Token object over the new socket
new_socket.send(serialized_updated_token)

# Close the sockets
#client_socket.close()
#server_socket.close()
new_socket.close()
