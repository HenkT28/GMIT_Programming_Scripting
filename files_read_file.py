# Open a file, for reading.
f = open('myfile.txt', 'r')

# To read the file.
s=f.read()

print(s)

# And you have to close it afterwards.
f.close()