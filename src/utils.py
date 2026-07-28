# This modules handles the various arithmetic operations we need
import random


# Security -> relies on an external function in it's codebase (is_prime)
# what i think -> move the logic in house or pass it by argument with correct handling
def prime_generator(size) :
    while True:
        num = random.getrandbits(size)
        if (num % 2) == 0:
            num += 1       
        if is_prime(num):
            return num
    return 

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
        print("e and phi are not coprime")
        return
    return x % phi

# security -> e value is too random
# what i think -> after research it seems 65537 is the best practice and randomness doesn't matter 
# security -> use of built in random 
# what i think -> appently it's not as random, further research needed 
def public_exponent(phi):
    e = random.randrange(1,phi)
    if e%2 == 0:
        e +=1
    while gcd(e,phi) != 1:
            e +=2
    return e       

