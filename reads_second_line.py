# Henk Tjalsma, 2019
# Solution to problem 1 - sumupto.py script
# Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line. 
# http://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0001
# I will only cover, Title: Moby Dick; or The Whale, CHAPTER 1, as example.
# Getting error when reading file: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
# The same when downloading this file: http://www.gutenberg.org/files/2701/2701-0.txt
# As this didn't work, file = open(filename, encoding="utf8"), I changed it to file = open(filename, errors='ignore')
# https://www.pythoncentral.io/reading-and-writing-to-files-in-python/
# https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po


# Open a file, for reading.
f = open('moby-dick.txt', 'r', errors = 'ignore')

# Make sure we're at the start of the file
f.seek(0)

# To read the file, and lines
lines = f.readlines()
# s=f.read()

# print(s)
print(lines[1])

# And you have to close it afterwards.
f.close()