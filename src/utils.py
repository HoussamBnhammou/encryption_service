import random
# this for the functions we will using across the files (gcd, mod, phi calc, etc...)
# i understand these are small operations and don't necessarly require a function of their own 
# but let's do it just to practice modularity and writing more human readable code


# FLAG: !!!!!!
# didn't implement the two primes, this one only returns 1 prime
# Answer flag : we start with this and make sure to do a duplicate check when we invoke this function twice
def prime_generator(size) :
    while True:
        num = random.getrandbits(size)
        
        # FLAG : !!!!!
        # if the random is even it adds 1 to it
        if (num % 2) == 0:
            num += 1
        
        if is_prime(num):
            return num
    return 

# i added safe guards against stupid input, this will always be correct
# not sure but i think we can make this alot more effcient somehow
# which will make the prime_generator() more efficient
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

# i know this might seem uncessary, it's to practice writing modular shit 
# also it's much better and faster to read euler_phi() than to look a math operation and figure out what it is
def euler_phi(p,q) :
    return (p - 1) * (q - 1) 

# greatest common divider
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# the one greatest common divider we truely need
def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

# FLAG: !!!!
# i don't know how to handle the case for e and phi not being co prime
# my intuition is to remove extended_gcd() and move the logic inside to pick co-prime numbers
# also i didn't test and not sure of it 
def modular_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    # handling if the two things are not coprime
    if g != 1:
        print("e and phi are not coprime")
        return
    return x % phi


def public_exponent(phi):
    e = random.randrange(1,phi)
    if e%2 == 0:
        e +=1
    while gcd(e,phi) != 1:
            e +=2

    return e       

