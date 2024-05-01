def get_first_sorted_name(names):
    names.sort()
    name = names[1]
    return name

# Arrange
names = ["Tina", "Peter", "Jack", "Jamie", "Anita"]
# Act
result = get_first_sorted_name(names)
# Assert
print(result)
print(result == "Anita")