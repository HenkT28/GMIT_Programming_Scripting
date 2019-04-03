# https://en.wikipedia.org/wiki/Factorial
# In mathematics, the factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n.
# Positive integer -> we wil verify if input is correct, non-negative integer

def fac(n):
    if n < 0:
        raise ValueError
# Variable ans -> identity value for multiplication
# Beginning of function   
    ans = 1

    while n > 0:
        ans = ans * n
        n = n -1

# When n is not greater than 0, it returns ans
    return ans
# End of function

# Below is outside of the function, the try and except block
# I'm calling the function -> fac(i)
for i in range(-10,10):
    try:
        print(i, "factorial is", fac(i))
    except ValueError:
        print (i, "is negative, factoral undefined.")    