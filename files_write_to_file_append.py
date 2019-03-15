# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# 'a' opens the file for appending
f = open('my_file_adding.txt', 'a')

# Below appends the line, Hello World!, and 2nd line, Goodbye, World!
# \n, means new line.
# On Windows you sometimes want to put in \r\n, that is because new line endings, new lines are slightly different on Windows than on MacOS, and linux.
# f.write("Hello, World!\r\nGoodbye, World!\r\n")
f.write("Hello, World!\nGoodbye, World!\n")

f.close()