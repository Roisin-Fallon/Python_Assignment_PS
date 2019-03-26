# Roisin Fallon, 2019 - 02 - 26
# Approximate a square root of a floating point number

rootof = 64

# The initial estimate for the square root
estimate = 6.0

# When your ((estimate * estimate) - rootof) will be zero (8 *8)-64 = 0
# As long as my estimate within 0.1 of the number it is considered a good estimate

# Keep going until the square of estimate is within 0.1 of root

while abs((estimate * estimate) - rootof) > 0.1:

# This is Newton's method to improve our estimate 
# Adopted from (https://tour.golang.org/flowcontrol/8)
    estimate -= ((estimate * estimate ) - rootof)/ (2 * estimate)

# Print the result
print(f"The square root of {rootof} is approx. {estimate}.")