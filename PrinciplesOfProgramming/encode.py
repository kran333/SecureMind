input_msg = input("Your message? ").upper()
encode_key = int(input("Encoding key? "))
encode_msg = ""
for cht in input_msg:
    ord_cht = ord(cht)
    if cht in (" ", '"', "!"):
        encode_msg += cht
    elif ord_cht+encode_key > 90:
        encode_msg += chr(64 + (encode_key - (90 - ord_cht)))
    elif ord_cht+encode_key < 65:
        encode_msg += chr(91 + (encode_key - (65 - ord_cht)))
    else:
        encode_msg += chr(ord_cht + encode_key)

print(encode_msg)
