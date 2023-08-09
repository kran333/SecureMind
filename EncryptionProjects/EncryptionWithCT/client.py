import hashlib

class Client:
    def __init__(self, rand_num, password, crypto_table):
        self.__rand_num = rand_num
        self.__password = password
        self.__crypto_table = crypto_table

    def __xor_operator(self):
        __result = 0
        while __result.bit_length() != self.__rand_num.bit_length():
            __result = self.__rand_num ^ self.__password
        return __result

    # Hash generator of SHA256
    def __hash_value_geneartor(self, input_data):
        input_data = str(input_data).encode('utf-8')
        __hash_object = hashlib.sha512(input_data)
        __msg_hex_dig = __hash_object.hexdigest()
        return __msg_hex_dig

    # Extracting the private key using Crypto Table cordinates
    def __private_key_extractor(self, cordinates):
        __private_key = ''
        for cord in cordinates:
            x_cod = int(cord[-1], 16)
            y_cod = int(cord[0], 16)
            __private_key += self.__crypto_table[x_cod][y_cod]
            __private_key += self.__crypto_table[y_cod][x_cod]
        return __private_key

    def client_driver_code(self):
        print(f"Client Side Public Key : {self.__rand_num} and it's Size is {self.__rand_num.bit_length()} bits")

        __xor_public_key = self.__xor_operator()
        print(f"Client Side Bitwise XOR: {__xor_public_key} and it's Size is {__xor_public_key.bit_length()} bits")

        __message_digest = self.__hash_value_geneartor(__xor_public_key)
        print(f"Client Side Message Digest is : {__message_digest} and Size is {len(__message_digest)}")

        __cordinates = [__message_digest[i:i + 2] for i in range(0, len(__message_digest), 2)]

        __private_key = self.__private_key_extractor(__cordinates)
        print(f"Client Side Private Key: {__private_key} and it's Size is {len(__private_key)}")
        return __private_key