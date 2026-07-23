# this for the functions we will using across the files (gcd, mod, phi calc, etc...)
# i understand these are small operations and don't necessarly require a function of their own 
# but let's do it just to practice modularity and writing more human readable code


# i like the thing about generating two in this function to avoid the risk of dups, good catch brother
# havn't made any research on efficiency, we can use is_prime() below along with random()
# i do remeber that you don't need to check until prime but only to sqrt(prime)
# this can make is_prime() faster if we end up using it 
def prime_generator(size) :
    return 

# to verify prime status, will be needed for the function above
# usually you assume whoever is going to use your products is trying to break it 
# i didn't since this just a basic attempt, so here is a guidline if have to use it :
# don't input 0,1,2 these are primes
# don't input even numbers, these are not primes
def is_prime(prime):
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

# i think this is the function that also generate coeff for the modular_inverse()
# to be done later
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# ntn so say here
def modular_inverse(e, phi):
    ##Houssam: currently working on this one but didn't lay out a line of code yet :/

    # todo
    return 

