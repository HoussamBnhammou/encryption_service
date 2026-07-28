# This module handles decryption 

# design -> padding is apparently common use here
# what i think -> needs more research 


def decryptor(ciphered, private_key):
    d, n = private_key
    chunk_size = (n.bit_length() - 1) // 8
    message = ""
    for i, ciphered_chunck in enumerate(ciphered):
        deciphered_chunck = pow(ciphered_chunck, d, n)
        if i < len(ciphered) - 1:
            message += str(deciphered_chunck).zfill(chunk_size)
        else:
            message += str(deciphered_chunck)
    return int(message)


