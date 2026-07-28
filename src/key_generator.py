# This module handles Key generation
from utils import *

# design and security -> recomputing the values for each file and no strength validation
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


# security -> e value is too random
# what i think -> after research it seems 65537 is the best practice and randomness doesn't matter 
# security -> use of built in random 
# what i think -> appently it's not as random, further research needed 
# Done: it seems like hard coding e donesn't affect security but also increase performance, on the other hand 
# with randomness there is a chance that "e" can be small, which can be exploited.
##Flag: even e is hardcoded, i suggest we leave a function for it in casae we changed our mind on it in the future.
def public_exponent(phi):
    return 65537