# Henk Tjalsma, 2019
# Solution to problem 9 - second.py moby-dick.txt
# Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.
 
# http://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0001
# I will only cover, Title: Moby Dick; or The Whale, CHAPTER 1, as example.

# Getting error when reading file: https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
# The same when downloading this file: http://www.gutenberg.org/files/2701/2701-0.txt
# This file is clean - https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
# As this didn't work, file = open(filename, encoding="utf8"), I changed it to file = open(filename, errors='ignore')

# https://www.pythoncentral.io/reading-and-writing-to-files-in-python/
# https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po
# https://stackoverflow.com/questions/16129650/what-does-x-2-0-mean

# Go through text file line by line.
with open('moby-dick.txt', 'r', errors = 'ignore') as f:
    count = 0
# For line in file.      
    for line in f:
        count+=1
# Below is the remainder operator (the condition, count % 2 == 0, checks if a number is even).        
        if count % 2 == 0: 
# Print line            
            print(line)