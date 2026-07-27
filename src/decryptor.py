## use the private key to decrypt the a message



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
    #input should be an encrypted message with private key and output should be the decrypted message
    return int(message)

## upgrade options :
# i don't think it's smart to have a function that takes the keys as params 
# i don't know how python handles stuff but in other languages we usually pass via an object
# or a read only instance or at worst reference and avoid storing the info somewhere 
