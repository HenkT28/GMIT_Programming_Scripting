# */* 
# What I want my program to do is to output let's say the sum of all the values,
# from say 0, or 1 up to i and including i. 
# *\*
i = int(input("Enter an integer: "))

if i == 0:
    print(0)
elif i == 1:
    print(1)
elif i == 2: 
# 3 because it's the sum of 0, 1, and 2     
    print(3)
elif i == 3:
# 6 because it's the sum of 0, 1, 2, and 3     
    print(6)
elif i == 4:
# 10 because it's the sum of 0, 1, 2, 3 and 4       
     print(10)       

# If you don't know how many elif clauses you need in an if statement, 
# that kind of situation is well suited, to what we call a while loop.