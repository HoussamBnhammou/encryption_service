## use the public key to encrypt the a message



def encryptor(message, public_key):
        # e: public exponent
        # n = multiplication of both prime numbers
        e, n = public_key
        chunk_size = (n.bit_length() -1 ) // 8
        message_string = str(message)
        ciphered_message = []
        for i in range(0,len(message_string), chunk_size):
                chunck_message = int(message_string[i:i+chunk_size])
                ciphered_chunck = pow(chunck_message, e , n)
                ciphered_message.append(ciphered_chunck)
        return ciphered_message

    #input should be a message with public key and output should be the encrypted message
    ## Flag: should we construct a conventional public key file, same goes for private key, i'd so we need to add logic to encode and decode a public and private key
    ## for now i am injecting the varibale needed as they are once it works we can iterate.

    ## mhammed response : 
    # i said smt in the decryptor module that i think anwsers your question.
    # but generally for encryption it's not an issue of keys but rather of the msg 
