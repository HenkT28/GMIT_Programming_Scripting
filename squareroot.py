# Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.
# Verbatim: https://www.geeksforgeeks.org/python-math-function-sqrt/
# https://www.programiz.com/python-programming/examples/square-root
# https://docs.python.org/3/tutorial/floatingpoint.html

n = float(input('Please enter a positive number: '))

if n < 0:
    print("Please enter a positive number.")
else:
   n_sqrt = n ** 0.5

print('The square root of %0.1f is approx. %0.1f'%(n ,n_sqrt))

# print("The square root of {} is {} ".format(n,n_sqrt))