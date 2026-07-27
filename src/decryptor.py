## use the private key to decrypt the a message



def decryptor(ciphered, d, n):
    message = ciphered.pow(d) % n
    #input should be an encrypted message with private key and output should be the decrypted message
    return message

## upgrade options :
# i don't think it's smart to have a function that takes the keys as params 
# i don't know how python handles stuff but in other languages we usually pass via an object
# or a read only instance or at worst reference and avoid storing the info somewhere 