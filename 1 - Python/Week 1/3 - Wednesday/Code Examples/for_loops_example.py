# Example 1
poke_list = ["Pikachu", "Charizad", "Gengar", "Squirtle"]

print(poke_list)
print("This is the list 👆")

for poke in poke_list:
    print("Current Pokemon: ", poke)

# # Example 2
random_sent = "Hello there General Kenobi"

for letter in random_sent:
    print(letter)

# Example 3
# range(6) = [1, 2, 3, 4, 5] - natural list
#               0 1 2 3 4  - true list as read in memory
for number in range(1, 6):
    print(number)

for number in range(0, 10, 2):
    print(number)

# Example 4
for i in range(1, 4):
    # print("Outer Loop postion: ", i)
    for j in range(1, 4):
        # print("Inner Loop position", j)
        print(i * j, end=" ")
    print()


# Example 5
random_sent = "Well, of course I know him. He's me"
random_sent_split = random_sent.split(" ")
print(random_sent_split)

for letter in random_sent_split:
    print(letter)