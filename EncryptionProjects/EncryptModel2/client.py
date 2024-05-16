import hashlib
import copy
from base import PWD, CT
from server import public_key as server_public_key


def __public_and_pwd_merger(rand_num, pwd):
    rand_num = str(rand_num)
    pwd = str(pwd)
    result = rand_num[0:len(rand_num) - len(pwd)] + pwd
    return result


# Hash generator of SHA256
def __get_hash_val(input_data):
    input_data = str(input_data).encode('utf-8')
    hash_object = hashlib.sha512(input_data)
    msg_hex_dig = hash_object.hexdigest()
    return msg_hex_dig

def __get_cords(message_digest):
    mid_val = int(len(message_digest)/2)
    first_half = message_digest[0:mid_val]
    second_half = message_digest[mid_val:]
    return [first_half, second_half]


# Extracting the private key using Crypto Table cordinates
def __extract_prik_ct(CT, MG_cords):
    private_key = ''
    for cord in range(len(MG_cords[0])):
        x = int(MG_cords[0][cord], 16)
        y = int(MG_cords[0][cord], 16)
        private_key += CT[x][y]
        private_key += CT[y][x]
    return private_key

def client_driver_code():
    print("................................ Client Side Implementation ................................")
    public_key = copy.copy(server_public_key)
    print(f"Client Public Key : {public_key}")
    print(f"Client Public Key Length : {public_key.bit_length()}")

    password = copy.copy(PWD)
    print(f"Client password : {password}")
    print(f"Client password Length : {password.bit_length()}")

    xor_public_key = __public_and_pwd_merger(public_key, password)
    print(f"Client public and pwd merge: {xor_public_key}")
    print(f"Client public and pwd merge Length : {len(xor_public_key)}")

    message_digest = __get_hash_val(xor_public_key)
    print(f"Client Message Digest Value : {message_digest}")
    print(f"Client Message Digest Length : {len(message_digest)}")

    crypto_table = copy.copy(CT)
    print("................Crypto Table.............")
    print(crypto_table.head())

    cords = __get_cords(message_digest)
    print(f"Client Cordinates for x: {cords[0]} and for y: {cords[1]}")

    private_key = __extract_prik_ct(crypto_table, cords)
    print(f"Client Private Key: {private_key}")
    print(f"Client Private Key length: {len(private_key)}")
    return private_key