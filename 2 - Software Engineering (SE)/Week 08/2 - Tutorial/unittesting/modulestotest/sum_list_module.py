def sum_list(num_list):
    """
    Sums up the elements in a list of numbers.

    Args:
        num_list (list): A list of numbers to be summed.

    Returns:
        int: The sum of all numbers in the list.
    """
    total = 0
    for num in num_list:
        total =+ num  # Use the += operator to update total from =+ num
    return total
