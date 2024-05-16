from server import server_driver_code
from client import client_driver_code

serv_priv_key = server_driver_code()
print("====================================================================================================================")
cli_priv_key = client_driver_code()
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
if serv_priv_key == cli_priv_key:
    print("Server's Private Key and Client's Private Key are Matching........!")
    print(f"Server: {serv_priv_key} \nClient: {cli_priv_key}")