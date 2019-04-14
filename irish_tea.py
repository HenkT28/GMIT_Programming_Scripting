# The objective of the task is to (using the Vim text editor) write a shell script program that behaves like an Irish person offering a cup of tea. 
# If the user types ‘y’ to the offer, the program displays “Great, I’ll make tea now” to the console. 
# If the user types ‘n’ to the offer, the program asks the user “Are you sure” 4 more times before giving up. 
# If at any point during the 4 follow up offers, the user changes their mind and presses ‘y’, the computer will print out “Great, I’ll make tea now” to the console. 

# In addition to shell scripting, this assignment examines your ability to use ‘while loops’ and’ if statements’ correctly. 
# It also examines your ability to research and locate the information required online. 

# Entering a positive integer by user.
# https://stackoverflow.com/questions/43088603/python-loop-and-invalid-answer

answer = input("Would you like a cup of tea? Yes, type y, or No, type n: ")

no = 0

while True:
    try:
        if answer.lower() == "y":
            print ("Great, I’ll make tea now")
            break 
        elif (answer.lower() == "n" and no != 4):
            print ("Are you sure?")
            answer = input("Yes, type y, or No, type n: ")
            no = no + 1
            continue
        else:
            print ("Ok, no worries")
            break         
    except ValueError:
        continue    


           
