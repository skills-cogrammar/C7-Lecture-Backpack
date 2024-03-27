# Example 1
try:
    var_one = int(input("Enter the number of muffins stolen: "))
    print(f"Drats! {var_one} muffins! That's more than 2 for sure!")
except ValueError:
    print("Enter an integer value e.g (34)")
except NameError as e:
    print(f"Error: {e}")

# Example 2
while True:
    try:
        user_order = int(input("Enter the number of muffins you want: "))
        if user_order > 1:
            print(f"You have ordered {user_order} muffins. Enjoy the rest of your day")
        else:
            print(f"You have ordered {user_order} muffin. Enjoy the rest of your day")
        break
    except ValueError:
        print("You have entered the value incorrectly. Enter an integer value e.g (34)")
