import math

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

def fast_modulo_power(n, power, mod):
    result = 1
    binary_power = bin(power)[2:]

    for i in range(len(binary_power)-1, -1, -1):
        if binary_power[i] == '1':
            result = result * n % mod
        n = n*n % mod

    return result

def factorize(n):
    result = []
    k=2
    while n > 1 and k < math.sqrt(n):
        while n%k == 0:
            result += [k, int(n/k)]
            n /= k
        k+=1
    return result

def find_generator(n):
    for m in range(2, n):
        for i in factorize(n):
            if fast_modulo_power(m, i/(n-1), n):
                break
        else:
            return m

###

number = 1000003

if is_prime(number):
    print("{} is prime\n".format(1000003))

print("Smallest generator is: {} \n".format(find_generator(number)))

print("Diffie-Hellman protocol:\n")

try:
    a = int(input("Pick private number for person A: "))
    b = int(input("Pick private number for person B: "))
    
    A = fast_modulo_power(2, a, number)
    B = fast_modulo_power(2, b, number)
    
    A_s = fast_modulo_power(B, a, number)
    B_s = fast_modulo_power(A, b, number)
    
    print("")
    
    print("Private key received by A is {}".format(A_s))
    print("Private key received by B is {}".format(B_s))
except Exception:
    print("wrong input")
