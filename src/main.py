##split the processes to key generation where we will handle all the process of private and public key generation
##then we have encryptor and decryptor module where we can use the keys to weather encrypt or deycrept the messages
from ascii_transformer import *
from encryptor import *
from decryptor import *
from utils import *
from key_generator import *

size = 9
message = "Heil Hitler"

ascii_message = stringToasci(message)

p = prime_generator(size)
q = prime_generator(size)

while p == q:
    q =  prime_generator(size)

n = p*q

e = generate_public_key(p, q)

d = generate_private_key(p, q, e)

ciphered_message = encryptor(message, e, n)

deciphered_message  = decryptor(ciphered_message, d, n)

final_deciphered_message = asciToString(deciphered_message)


print(message)
print(p)
print(q)

print(e)
print(d)
print(ciphered_message)
print(deciphered_message)
print(final_deciphered_message)
