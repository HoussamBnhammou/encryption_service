# This modules handles the various arithmetic operations we need
import random


# Security -> relies on an external function in it's codebase (is_prime)
# what i think -> move the logic in house or pass it by argument with correct handling
# answer: i don't think that's really a cencernt, relying on function that exist not only on 
# the same code base but also in the same file, i wouldn't be treat it as an external function

# the primality efficient test check up require to iterate through the first 100 prime numberes
first_hundred_primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

def prime_generator(n) :
    while True:
        num = random.randrange(2**(n-1) + 1, 2**n - 1) 
        #that's the range of numbers with n bits, where the strongest bit is 1.  and it is odd
        if is_prime(num):
            return num

# Complexity -> limits the size of the key 
# what i think -> needs research, i know for sure there are better ones
def is_prime(prime):
    if prime < 2:
        return False
    if prime == 2:
        return True
    if prime % 2 == 0:
        return False
    i = 3
    while i * i <= prime:
        if prime % i == 0:
            return False
        i += 2
    return True
    ## commented the new logic  until we i fully finish a proper working implementation then i remove the old logic.
    # for divisor in first_hundred_primes:
    #     if prime % divisor == 0 and divisor**2 <= prime: 
    #         return False

def isMillerRabinPassed(prime):
    #  i was reading and understing the implementaion of rabin test but the clock was clocking. i will finish from here next time/
    return



def euler_phi(p,q) :
    return (p - 1) * (q - 1) 


def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

# design -> handles failure using printf() 
# what i think -> pretty self evident, gotta implement the python version of stderr 
def modular_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("e and phi are not coprime")
    return x % phi

     

