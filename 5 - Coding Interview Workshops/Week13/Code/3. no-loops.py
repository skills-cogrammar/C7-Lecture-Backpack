# Third diagram in the planning file

def get_final_order(children: list, moves: int):
    last_wrapper_index = len(children) - (moves % len(children))
    return children[last_wrapper_index:] + children[:last_wrapper_index]

children = [1, 2, 3, 4, 5]
move = 11

output = get_final_order(children, move)
print(output)