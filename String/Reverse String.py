# Reverse String

#You must do this by modifying the input array in-place with O(1) extra memory
#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
def reverseString(s):
    t = len(s)-1
    i = 0
    while t >= i:
        x = s[i]
        s[i] = s[t]
        s[t] = x
        t = t - 1
        i = i + 1
    return s

#s = ["H","a","n","n","a","h"]
s = ["h","e","l","l","o"]
print(reverseString(s))
#print(s[::-1])