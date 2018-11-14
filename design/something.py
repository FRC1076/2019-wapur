# x_list = ["x"] * 10
# y_list = ["y"] * 10
# big_list = [x_list + y_list]
# print(big_list)

# name = "Jason Bourne"

# if (name == "Jason Bourne"):
#     print("jesus christ its jason bourne")

# old_password = "old"
# current_password = "current"
# password = input()

# if (password == current_password):
#     print("correct")
# elif (password == old_password):
#     print("outdated")
# else:
#     print("wrong")

# for x in range(5):
#     print(x)
# print(" ")
# for x in range(3,6):
#     print(x)
# print(" ")
# for x in range(3,8,2):
#     print(x)

# count = 0

# while count < 5:
#     print(count)

#     count += 1

# items = ["a","b","c"]
# askforinput = True

# while(1):
#     if(askforinput):
#         askforinput = False
#         user_input = input()
#         if (user_input in items):
#             print("correct")
#         else:
#             print("wrong")
#             askforinput = True

range_list = list(range(0,100))

for item in range_list:
    if item % 7 == 0:
        print(item, " is divisible by 7")

