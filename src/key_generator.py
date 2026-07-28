# This module handles Key generation
from utils import *

# design and security -> recomputing the values for each file and no strenth validation
# what i think -> we have to compute once, validate the key strength right here as well



# security -> p != q check is offloaded to the main 
# what i think -> just add a line here with proper error handling 
def generate_public_key(p,q):
    n = p * q
    phi = euler_phi(p, q)
    e = public_exponent(phi)
    return (e, n)

# security -> same here, p != q check is offloaded to the main 
# what i think -> just add a line here with proper error handling 
def generate_private_key(p,q,e):
    n = p * q
    phi = euler_phi(p, q)
    d = modular_inverse(e, phi)
    return (d, n)
