def summation_of_primes(primes):
    suma = 0
    for i in range(2, primes+1):
        cont = 0
        for j in range(1, i+1):
            if i % j == 0:
                cont += 1
        if cont == 2:
            suma += i
    return suma

if __name__ == '__main__':
    print(summation_of_primes(5))
    print(summation_of_primes(6))
    print(summation_of_primes(7))
    print(summation_of_primes(8))
    print(summation_of_primes(9))
    print(summation_of_primes(10))
    print(summation_of_primes(20))