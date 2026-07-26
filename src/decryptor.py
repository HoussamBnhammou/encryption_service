## use the private key to decrypt the a message



def decryptor(ciphered, d, n):
    message = ciphered.pow(d) % n
    #input should be an encrypted message with private key and output should be the decrypted message
    return message

