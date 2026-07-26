## use the public key to encrypt the a message



def encryptor(message, e, n):
        # e: public exponent
        # n = multiplication of both prime numbers
        ciphered = message.pow(e) % n
        return ciphered

    #input should be a message with public key and output should be the encrypted message
    ## Flag: should we construct a conventional public key file, same goes for private key, i'd so we need to add logic to encode and decode a public and private key
    ## for now i am injecting the varibale needed as they are once it works we can iterate.
