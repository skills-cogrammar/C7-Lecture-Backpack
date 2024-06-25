class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def show_graph(self):
        for vertex, list in self.adjacency_list.items():
            print(f'{ vertex } -> { list }')


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

my_graph.add_edge("A","B")
my_graph.add_edge("B","D")
my_graph.add_edge("A","C")
my_graph.add_edge("C", "D")

if __name__ == "__main__":
    my_graph.show_graph()

