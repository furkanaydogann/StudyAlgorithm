#Given an integer n, return a string array answer (1-indexed) where:

#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i (as a string) if none of the above conditions are true.

def fizzbuzz(n):
    i = 1
    c = n
    n = []
    while i <= c:
        if i % 3 == 0 and i % 5 == 0:
            n.append("FizzBuzz")
        elif i % 3 == 0:
            n.append("Fizz")
        elif i % 5 == 0:
            n.append("Buzz")
        else:
            n.append(str(i))
        i = i+1
    return n

n = 20
print(fizzbuzz(n))
