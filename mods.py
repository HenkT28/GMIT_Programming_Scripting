import datetime as dt
import csv
import math

# Create a filename from the current date and time.
filename = dt.datetime.strftime(dt.datetime.now(),"%Y-%m-%d-%H-%M-%S.csv")

# Open the file with that filename.
with open(filename, 'w', newline='') as f:
    # Enable CSV writing to the file.
    writer = csv.writer(f)
    # Write a header row.
    writer.writerow(["i", "j", "gcd"])
    # Write the GCD for all (i,j) pairs from o to 100.
    # So for every value of i, j will start at 0, and count all the way up to but not including 100 (10000 times).
    for i in range(100):
        for j in range(100):
            writer.writerow([i, j, math.gcd(i, j)])