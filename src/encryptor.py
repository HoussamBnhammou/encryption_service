# This module handles encryption 

# design -> padding is apparently common use here
# what i think -> needs more research 
# P.S. : my session timer just ended, i didn't actually read and thouroughly verify this function

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
