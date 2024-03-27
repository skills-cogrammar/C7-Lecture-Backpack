# Example 1

# list_of_cats.txt  - relative path
# C:\Users\smugh\Desktop\session_workspace\list_of_cats.txt - absolute path

# traditional method (explicit)
# file = open("list_of_cats.txt", 'r')
# file.close()

# newer (implicit)
# with open("list_of_cats.txt", 'r') as file:
#     # print(file)
#     pass

# Example 2
# Reading from file
# with open("random_phrase.txt", 'r') as file:

#     file_content = file.readlines()

#     for line in file_content:
#         print(line)

#     first_line = file_content[0]
#     print(f"The first line is: {first_line}")

    # content = file.read()
    # print("\nThis is the read() output: ")
    # print(content)

    # file.seek(0)

    # content = file.readline()
    # print("\nThis is the readline() output: ")
    # print(content)

    # file.seek(0)
    
    # content = file.readlines()
    # print("\nThis is the readlines() output: ")
    # print(content)


# read()
# readline()
# readlines()
    
# writing to file
with open("cats.txt", 'w') as file:
    user_cat = input("What is your cat's name ? ")
    file.write(f"\n{user_cat}")

    # content = file.readlines()
    m_cats = ["Mitzy", "Speckle", "Archie", "Mimas"]
    r_cats = ["Mushu", "Willow", "Kion"]
    # file.writelines(m_cats)

    for line in r_cats:
        file.write(f"\n{line}")

# Challenge: Prompt the user for a cat's name, add it to a list, and make sure the list is sorted alphabetically.