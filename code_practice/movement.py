from random import *
x = randint(-5, 5)
y = randint(-5, 5)
treasurecoords = (x, y)
print(treasurecoords)
a = 0
b = 0
print(
    "n = north, s = south, w = west, e = east, ne = northeast, se = southeast, sw = southwest, nw = northwest."
)
coords = (a, b)
direction = 9
while coords != treasurecoords and direction != "stop":
    direction = input("Which direction will you travel?:")

    def directioncalc():
        if direction == "n":
            return 1
        elif direction == "ne":
            return 2
        elif direction == "e":
            return 3
        elif direction == "se":
            return 4
        elif direction == "s":
            return 5
        elif direction == "sw":
            return 6
        elif direction == "w":
            return 7
        elif direction == "nw":
            return 8
        else:
            return 0

    directioncalc = directioncalc()

    xa = [2, 3, 4]
    xb = [6, 7, 8]
    xc = [1, 5]

    def movementcalc1(a):
        if directioncalc in xc:
            return (a)
        elif directioncalc in xa:
            return (a + 1)
        elif directioncalc in xb:
            return (a - 1)
        else:
            print("that is not a valid directional input.")
            return a

    ya = [1, 2, 8]
    yc = [4, 5, 6]

    def movementcalc2(b):
        if directioncalc in ya:
            return (b + 1)
        elif directioncalc in yc:
            return (b - 1)
        else:
            return b

    a = movementcalc1(a)
    b = movementcalc2(b)

    if a > 5:
        print("Hey, you can't leave the map!")
        a = 5
    elif a < -5:
        print("Hey, you can't leave the map!")
        a = -5
    if b > 5:
        print("Hey, you can't leave the map!")
        b = 5
    elif b < -5:
        print("Hey, you can't leave the map!")
        b = -5
        coords = (a, b)
    print("your coordinates are:")
    print(a, b)
    if coords == treasurecoords:
        print("Congrats, you won the treasure!")
