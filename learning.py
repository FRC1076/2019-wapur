#Learning Python

mylist = [1, 3, 4, 7, 4, 9]

print(mylist[0], mylist[4])

x = 225

evenNumbers = [2, 4, 6, 8]
oddNumbers = [1, 3, 5, 7]

newlist = []


def bettersort(listtosort):
    newlist = []
    #While listtosort has values,
    #check wether x is before the first value
    #If so, move to value 0
    #repeat until finished
    while listtosort:
        minimum = listtosort[0]
        for x in listtosort:
            if x < minimum:
                minimum = x

        newlist.append(minimum)
        listtosort.remove(minimum)
    return newlist


list1 = ["joe", "bob"]
list2 = ["greg", "william"]

biglist2 = bettersort(list1 + list2)
print(biglist2)


def Register():
    name = input('Enter your name')
    age = input('Enter your age')
    users = ["bob", "joe"]
    if (name in users and int(age) > 5):
        print("You are allowed in")
    elif (name not in users):
        yes = input("Would you like to register? (yY or nN) ")
        if (yes == 'y' or yes == 'Y'):
            users.append(name)
            print("You have been registerd")
        else:
            print("Good By")
    else:
        print("You are not old enough")
