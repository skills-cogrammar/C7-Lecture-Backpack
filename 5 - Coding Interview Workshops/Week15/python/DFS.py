from AjacencyList import my_graph


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)  # Process the node
            visited.add(node)
            # Add neighbors to the stack in reverse order to maintain correct traversal order
            stack.extend(reversed(graph.adjacency_list[node]))



dfs_iterative(my_graph, "A")