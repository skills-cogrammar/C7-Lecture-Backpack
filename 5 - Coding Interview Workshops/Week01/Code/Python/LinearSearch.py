# Python Code
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [4, 2, 8, 5, 1, 9, 3]
target = 1
result = linear_search(arr, target)
if result != -1:
    print("Element found at index {}.".format(result)) 
else:
    print("Element not found")