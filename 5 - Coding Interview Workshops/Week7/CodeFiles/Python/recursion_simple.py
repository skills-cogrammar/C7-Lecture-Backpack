def tail_factorial (current_number , previous_multiplication = 1):
    if current_number <= 0:
        return previous_multiplication
    else:
        return tail_factorial( current_number - 1, current_number * previous_multiplication )

def rec_factorial(n):
    if n <=0: 
        return 1
    else:
        return n * rec_factorial(n - 1)

def rec_sum(x):
    if (x == 0):
        return 0
    else:
        return x + rec_sum(x - 1)

def tail_rec_sum(x, running_total = 0):
    if (x == 0):
        return running_total
    else:
        return tail_rec_sum(x - 1, running_total + x)

def iter_factorial(n):
    fact = 1
    while (n > 0):
        fact = fact * n
        n = n - 1
    return fact

print(tail_rec_sum(100))
print(tail_factorial(5))
print(rec_sum(100))
print(rec_factorial(5))
# print(iter_rec_sum(100))
print(iter_factorial(5))


