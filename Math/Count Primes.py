#Given an integer n, return the number of prime numbers that are strictly less than n.

def countPrimes(n):
    counter = 0
    for i in range(2, n + 1):
        div = 0
        for j in range(2, i):
            if i % j == 0:
                div = div + 1
        if div == 0:
            counter = counter + 1
    return counter




n = 10
print(countPrimes(n))
