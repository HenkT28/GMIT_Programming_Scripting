for n in range(2, 10):
    for x in range(2, n):
# In below they say if N, which is the outer number, modulo so give me the remainder, divide N by X, which is the value from the inner for loop.
# So n module x, so if the remainder, from dividing n by x, is equal to 0, then print...
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')