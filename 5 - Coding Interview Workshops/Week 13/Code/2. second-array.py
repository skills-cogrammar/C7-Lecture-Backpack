# Second diagram in the planning
from array import array # Array documentation https://www.w3resource.com/python/library/python_array_module.php

def get_final_order(children: array, moves: int):
    final_order = array('i', [0] * len(children)) # Simulates creating an empty arry of children length

    for seat, child in enumerate(children):
        next_seat = (seat + moves) % len(children) # Modulus to wrap around
        final_order[next_seat] = child # Add child to final order

    return final_order

children = array('i', [1, 2, 3, 4, 5])
move = 8

output = get_final_order(children, move)
print(output)
            

            


            
