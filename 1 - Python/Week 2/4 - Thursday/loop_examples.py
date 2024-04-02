# Example 1
# count = 5

# while count > 0:
#     print(count)
#     count -= 1

# print("takeoff")


# Example 2
# while True:
#     user_var = input("Enter a name: ")

#     if user_var != "Luke":
#         print("try again")
#     else:
#         print("Correct, you may now leave")
#         break

# Example
attempts = 0
# while True:
#     user_prompt = input("Enter your password: ")

#     if user_prompt == "a1b2c3":
#         print("welcome")
#         break
#     elif attempts >= 2:
#         print("Incorrect password entered multiple times. ")
#         break
#     else:
#         print("Incorrect password")
#         attempts += 1

while attempts != 3:
    user_prompt = input("Enter your password: ")

    if user_prompt == "a1b2c3":
        print("welcome")
        break
    else:
        attempts += 1