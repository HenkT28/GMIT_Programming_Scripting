# Approximate a square root using Newton's method.
# Henk Tjalsma

# The number to calculate the square root of.
rootof = 64.0
# The initial estimate for the square root.
estimate = 6.0


# abs -> Absolute value 
# abs -> Takes a positive value and leaves it unchanged, takes negative number and turns it into positive number)
# Keep going until the square of estimate is within 0.1 of rootof.
while abs((estimate * estimate) - rootof) > 0.1:
    # This is Newton's method to improve our estimate.
    # Adapted from: https://tour.golang.org/flowcontrol/8
    estimate -= ((estimate * estimate) - rootof) / (2 * estimate)

# Print the result.
print(f"The square root of {rootof} is approx. {estimate}")