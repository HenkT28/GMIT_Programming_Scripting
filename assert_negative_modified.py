# https://en.wikipedia.org/wiki/Factorial
# In mathematics, the factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n.
# Positive integer -> we wil verify if input is correct, non-negative integer

def fac(n):
# We are asserting, making sure n has a value greater than 0.    
    assert n >= 0
   
# Variable ans -> identity value for multiplication
# Beginning of function   
    ans = 1

    while n > 0:
        ans = ans * n
        n = n -1

# When n is not greater than 0, it returns ans
    return ans
# End of function

for i in range(-10,10):
    print (i, "factoral is", fac(i))    