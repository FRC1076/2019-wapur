import functions_variables
import random

# Given a direction the robot is facing, find the direction
# that the robot would then be facing if the robot turned right.

init_direction = random.randint(0, 3)
fin_direction_right = None
fin_direction_left = None

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

#-------------------------------------------------------------------#
# Do tests and set a result using if/else if... what direction is it facing if it turns right?

#print your final direction

#-------------------------------------------------------------------#
# Now try a solution that uses modulus

#print your final direction

#-------------------------------------------------------------------#
# How do we compute what left facing is?


#-------------------------------------------------------------------#
# Put your algorithms inside functions
def direction_to_right(direction):
    ...


def direction_to_left(direction):
    ...


# Use our mapping function!
to_right = [EAST, SOUTH, WEST, NORTH]
to_left = [WEST, NORTH, EAST, SOUTH]

# Dictionaries to store arrays?
