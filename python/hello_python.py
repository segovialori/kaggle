######## KAGGLE COURSES ########
#### HELLO, PYTHON ####
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter / 2
# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = (pi) * (radius ** 2)

########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

######################################################################
a, b = b, a

# 4.
# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves.
# For the sake of their friendship, any candies left over will be smashed. For example, if they collectively
# bring home 91 candies, they'll take 30 each and smash 1.

# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.
# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies

to_smash = (alice_candies + bob_candies + carol_candies) % 3
to_smash

# Complete the body of the following function according to its docstring.
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    rounded = round(num, 2)
    return rounded

# 3. In the previous exercise, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
#
# Below is a simple function that will calculate the number of candies to smash for any number of total candies.
#
# Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
#
# Update the docstring to reflect this new behaviour.

def to_smash(total_candies, total_friends = 3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.

    >>> to_smash(91)
    1
    """
    return total_candies % total_friends

# Booleans and conditionals

# 1.  Many programming languages have sign available as a built-in function. Python doesn't, but we can define our own!

# In the cell below, define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0
#2.
if total_candies == 1:
    print("Splitting 1 candy")
else:
    print("Splitting", total_candies, "candies")
Here's a slightly more succinct solution using a conditional expression:

print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")