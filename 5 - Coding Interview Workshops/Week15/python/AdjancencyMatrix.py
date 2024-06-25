'''
[0, 1, 0, 0, 0]
[1, 0, 0, 0, 1]
[0, 0, 0, 1, 0]
[0, 0, 1, 0, 0]
[0, 1, 0, 0, 0]
'''
class Graph:
    def __init__(self, no_of_vertices):
        self.no_of_vertices = no_of_vertices
        self.adjacency_matrix = [[0] * no_of_vertices for _ in range(no_of_vertices)]
        self.vertex_data = [''] * no_of_vertices

    #undirected unweighted
    def add_edge(self, vertex1, vertex2):
        self.adjacency_matrix[vertex1][vertex2] = 1
        self.adjacency_matrix[vertex2][vertex1] = 1

    def add_vertex_data(self, vertex, data):
        self.vertex_data[vertex] = data

    def show_graph(self):
        for i in range(self.no_of_vertices):
            print(f'{self.vertex_data[i]} {self.adjacency_matrix[i]}')


my_graph = Graph(5)
my_graph.add_edge(0,1)
my_graph.add_edge(2,3)
my_graph.add_edge(1,4)
my_graph.add_vertex_data(0, "A")
my_graph.add_vertex_data(1, "B")
my_graph.add_vertex_data(2, "C")
my_graph.add_vertex_data(3, "D")
my_graph.add_vertex_data(4, "E")


if __name__ == "__main__":
    my_graph.show_graph()




