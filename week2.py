print("Play Brawlhalla with me")
x = 5
print (x)
myStr = "Play Brawlhalla with me"
print (myStr)
one = 1
two = 2
three = one + two
print(three)
H = "Hello"
W = "World"
Greetings = H + " " + W
print (Greetings)

a,b = 3,4
print (a,b)

mylist = []
mylist.append(1)
mylist.append("...")
mylist.append(3)
mylist.append(6)
mylist.append(4)
print(mylist[0])
print(mylist[1])
print(mylist[4])
for i in mylist:
    print(i)

Numbers = []
Strings = []
Names = ["bob", "charlie", "name"]
print (Names)
Squared = 16 ** 2 - 1
print (Squared)

even_numbers = [2,4,6,8,]
odd_numbers = [1,3,5,7,]
all_numbers  = even_numbers + odd_numbers
print (all_numbers)
all_numbers.sort
print(all_numbers)
newList = [1,2,3]
print (newList * 3)

print (sorted(newList))

x_list = ["x"]*10
y_list = ["y"]*10
big_list = x_list + y_list
print(x_list)
print(y_list)
print(big_list)

name = "John"
if name in ["John", "Rick"]:
    print("your name is either john or rick")

answer = input("what is the best fighting game on steam?")
if answer == "Brawlhalla":
    print("You are a god!")
else:
    print ("you're bad")

x = [1,2,3]
print(x is [1,2,3])

for x in range(5):
    print(x)

for x in range(3,6):
    print(x)

for x in range(3,8,2):
    print(x)

names = ["John", "Joe", "Jerry"]
user_input = input("What is your name?")
if user_input in names:
    print ("Your name is either John, Joe, or Jerry.")
else:
    print ("Your name is not John, Joe, or Jerry. You're bad.")
    range_input = input("What range for multiples of 4?")
    myList = list(range(0,int(range_input)))
    for item in myList:
        if item % 4 == 0: print (item, " is divisible by 4")