"""
*
**
***
****
*****
****
***
**
*
"""

# print("#" + "#" + "#")

# Approach 1
star = "*"
# [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    if i >= 5:
        star = star[:-2]

    print(star)
    star += "*"

# Approach 2
star = "*"
for i in range(10):
    print(star)
    if i < 4:
        star += "*"
    else:
        star = star[:-1]

# Creating random phrase
random_phrase = "The quick brown fox jumps over the lazy dog"
print(random_phrase)


# using the split function will create a list of words, since we split by space
split_phrase = random_phrase.split(" ")
print(split_phrase)

# Join method can be used to join by specific character, in this case it is a '-'
split_phrase_joined = "-".join(split_phrase)
print(split_phrase_joined)
