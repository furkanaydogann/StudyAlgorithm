# Reverse String

r = []
def reverseString(s):
    t = len(s)-1
    while t >= 0:
        r.append(s[t])
        t = t - 1

    return r

#s = ["H","a","n","n","a","h"]
s = ["h","e","l","l","o"]
print(reverseString(s))
#print(s[::-1])