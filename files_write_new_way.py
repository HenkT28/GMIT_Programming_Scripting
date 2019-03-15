# It is good practice to use the with keyword when dealing with file objects. 
# The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point.
with open('myfile_new_way.txt', 'a') as f:
    f.write("This is from the new way!\n")
    f.write("Another line!")

print("The file is now closed.")
