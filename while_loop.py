i = int(input("Enter an positive integer: "))

total = 0

while i > 0:
# The new total value is on left hand side, old total on the right hand side.    
    total = total + i
    i = i -1

print(total)    