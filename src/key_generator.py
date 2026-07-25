#### this module is reponsible for genrating the priivate key and public key for encryption and decryption
from utils import *



# i was speed runing this shit
# please double check
def generate_public_key(p,q):
    n = p * q
    phi = euler_phi(p, q)

    # FLAG : !!!!
    # need a function to generate this one
    #added the e generator
    e = public_exponent(phi)


    return (e, n)


#double check please brother if you have time
def generate_private_key(p,q,e):
    n = p * q
    phi = euler_phi(p, q)

    d = modular_inverse(e, phi)

    return (d, n)
