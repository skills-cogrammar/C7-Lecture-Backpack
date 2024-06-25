from AjacencyList import my_graph
from collections import deque

def bfs(graph, start_point):
    queue = deque([start_point])
    visited_vertices = set()
    visited_vertices.add(start_point)

    while queue:
        popped = queue.popleft()

        print(popped)

        for item in graph.adjacency_list[popped]:
            if item not in visited_vertices:
                queue.append(item)
                visited_vertices.add(item)


bfs(my_graph, "A")