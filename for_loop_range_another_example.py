# Let's say I want to print the square of all below numbers

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] -> not needed. It gets automatically generated.

# for something in l, means, go through each of the elements in l, one by one.
# i, is a name you've made up...that's the name I want you to call the current element of the list, that I'm looking at.
for i in range(2, 10, 3):
    sq = i * i
    print("The square of", i, "is", sq)

print("Have a nice day!") 