# Go through text file line by line.
with open('my_file_line_by_line.txt', 'r') as f:
# For line in file.    
    for l in f:
# Print 2 copies of the line.        
        print(l,l)