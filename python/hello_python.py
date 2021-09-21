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

#4
# It does not have the second argument to round two places, function not defined, and there is a grammatical error
# ruound_to_two_places(9.9999)

def round_two_places(num):
    """
    This function will take in a number and round to two decimal places
    """
    return round(num, 2)

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0 # Your code goes here (try to keep it to one line!)


def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return ketchup ^ mustard 

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    total = int(ketchup) + int(mustard) + int(onion)
    return total == 1

#Lists
