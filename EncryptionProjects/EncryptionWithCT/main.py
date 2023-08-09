from server import Server
from client import Client
from common import CommonRnCt

# Declaring the initial values
input_msg_size = 256
pwd_size = 8
table_size = 64

# Creating the Random Number, Password, Cryptographic Table
comm_obj = CommonRnCt()
RNG = comm_obj.get_random_number(input_msg_size)
PWD = comm_obj.get_random_number(pwd_size)
CT = comm_obj.crypto_table(table_size)
print("####################################### CRYPTOGRPHIC TABLE USED FOR THIS INSTANCE #######################################")
print(CT.head(10))
print(f"Table Size is {table_size} X {table_size}")
print("******************** PASSWORD FOR THE SERVER AND CLIENT FOR THIS INSTANCE ********************")
print(f"Password: {PWD} and it's size is {pwd_size} bits")

# Server Object
print("======================================= SERVER SIDE ENCRYPTION =======================================")
server_obj = Server(RNG, PWD, CT)
server_private_key, server_public_key = server_obj.server_driver_code()

# Client Object
print("======================================= CLIENT SIDE DECRYPTION =======================================")
client_obj = Client(server_public_key, PWD, CT)
client_private_key = client_obj.client_driver_code()

# Validating the Server Private Key and Client Private Key
print("============================ VALIDATING Server Side and Client Side PRIVATE KEYS =====================")
if server_private_key == client_private_key:
    print("SERVER SIDE AND CLIENT SIDE PRIVATE KEYS MATCHED :)")
    print(f"Server Private Key: {server_private_key}")
    print(f"Client Private Key: {client_private_key}")
else:
    print("PRIVATE KEYS ARE NOT MATCHING :(")
