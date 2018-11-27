import functions_variables
# Given a direction the robot is facing, find the direction
# that the robot would then be facing if the robot turned right.
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# Do tests and set a result using if/else if 

if (direction = 0)









# Now try a solution that's a single expression and uses modulus
right = (facing + 1) % 4

# Then see if they can figure out how to compute what left
# facing is from this.
left = ???

# Then discuss how you can use an array to do a mapping
# function. (provided elements can be used as an index)
# See if they can figure it out.
to_right = [ EAST, SOUTH, WEST, NORTH ]
to_left = [ WEST, NORTH, EAST, SOUTH ]

# You could also show them how to use a dictionary to store
# the mapping.  (if dictionaries are on the agenda)

# Then show them how to put this inside a couple of functions
# so that it is easily reused.
def direction_to_right(dir):
	...
