for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
# Break will break you out of your for loop or while loop instantaneously, while continue is different continue says never mind continuing on with this. 
# Never mind the rest of the statements in this iteration, continue on with the rest of the for loop or continue on trying to run your while loop.   
# Continue jumps you back up to the first line. Break says break out of the for loop. Now it's interesting here break is actually breaking of the inner loop not the outer. 
#      
        continue
    print("Found a number", num)
