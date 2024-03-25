#Strings
text = 'codingforfun'
print('capitalize:',text.capitalize())

#Indexing, slicing
print(text[:4]) #prints all indexes till index 4
print(text[-3:]) #negative indexing, prints all indexes from -3 onwards

#Strip
text= ' codingforfun '
print(text.strip())
#Try rstip and lstrip

#Strip specific characters
txt = ',,,,,2,,1,rtgbananarr....'
x = txt.strip('1,2.rtg')
print(x)

#String formatting
random_word = 'Spanish Inquistion'
formatted_string = f"Nobody wants the {random_word}"
print(formatted_string)