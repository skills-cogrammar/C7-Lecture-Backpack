"""Now, let's import these modules into another script main.py and 
resolve the naming conflicts using aliasing:
"""

# Importing modules with aliasing
import modlib.mod_module1 as m1
import modlib.mod_module2 as m2
import modlib.mod_module3 as m3

# Using the sort functions from each module
data1 = [3, 1, 2]
sorted_data1 = m1.sort(data1)

data2 = [7, 5, 6]
sorted_data2 = m2.sort(data2)

data3 = [9, 8, 10]
sorted_data3 = m3.sort(data3)

# Printing the sorted data
print("Sorted data from module1:", sorted_data1)
print("Sorted data from module2:", sorted_data2)
print("Sorted data from module3:", sorted_data3)
