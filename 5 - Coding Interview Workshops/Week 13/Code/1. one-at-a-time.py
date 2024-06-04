# First series of diagrams in the planning

def get_final_order(children: list, moves: int):
    standing = None # There are no children standing initially
    
    for i in range(moves): # We will move the children forward
        for seat, child in enumerate(children): # We will iterate over the children

            # Set the child who is standing to the child who needs to find a seat
            if standing:
                child = standing
            
            # When we reach the end of the line, the last child should be standing 
            # So we can take them to the start of the line
            if seat + 1 == len(children):
                children[0] = child
                continue # No need to ask anyone to stand

            # We know as a fact that there will be a child in the next seat 
            # We will need that child to stand up so that the current child can 
            # claim that seat
            standing = children[seat + 1]
            children[seat + 1] = child

    return children

children = [1,2,3,4,5]
move = 7

output = get_final_order(children, move)
print(output)
