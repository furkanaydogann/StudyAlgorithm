#Given an integer n, return true if it is a power of three. Otherwise, return false.

#An integer n is a power of three, if there exists an integer x such that n == 3x.

#Input: n = 27
#Output: true

#Input: n = 0
#Output: false

def coinChange(x):
    counter = 0
    control = 1
    j = x
    while j > 2:
        if j % 3 == 0:
            counter = counter + 1
            j = j / 3
        else:
            j = j - 1
    for z in range(0, counter):
        control = control * 3

    if control == x and x != 1:
        return True
    else:
        return False





n = 82

print(coinChange(n))