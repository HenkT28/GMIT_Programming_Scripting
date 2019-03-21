import sys

# All you get is a list containing a single string. 
# print(sys.argv)

print(f"Script is called {sys.argv[0]}.")

for arg in sys.argv:
    print(arg)