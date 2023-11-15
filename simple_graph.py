from stack_queues import Queue

# Vertex class for the graph


class Vertex:

    # Initialize the vertex with a value and an empty list of adjacent vertices
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []

    # Add an adjacent vertex to the vertex's list of adjacent vertices
    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)

    # Print adjacent vertices for a particular vertex
    def print_adjacent_vertices(self):
        for vertex in self.adjacent_vertices:
            print(vertex.value)


class Graph:

    # Depth-first search traversal
    def dfs_traverse(self, vertex, visited_vertices={}):
        visited_vertices[vertex.value] = True
        print(vertex.value)
        for adjacent_vertex in vertex.adjacent_vertices:
            if visited_vertices.get(adjacent_vertex.value, False):
                continue
            self.dfs_traverse(adjacent_vertex, visited_vertices)

    # Depth-first search
    def dfs(self, vertex, search_value, visited_vertices={}):
        if vertex.value == search_value:
            return vertex
        visited_vertices[vertex.value] = True
        for adjacent_vertex in vertex.adjacent_vertices:
            if visited_vertices.get(adjacent_vertex.value, False):
                continue
            if adjacent_vertex.value == search_value:
                return adjacent_vertex
            vertex_were_searching_for = self.dfs(
                adjacent_vertex, search_value, visited_vertices)
            if vertex_were_searching_for:
                return vertex_were_searching_for
        return None

    # Breadth-first search traversal
    def bfs_traverse(self, starting_vertex):
        queue = Queue()
        visited_vertices = {}
        visited_vertices[starting_vertex.value] = True
        queue.enqueue(starting_vertex)
        while queue.read():
            current_vertex = queue.dequeue()
            print(current_vertex.value)
            for adjacent_vertex in current_vertex.adjacent_vertices:
                if adjacent_vertex.value not in visited_vertices:
                    visited_vertices[adjacent_vertex.value] = True
                    queue.enqueue(adjacent_vertex)

    # Breadth-first search
    def bfs(self, starting_vertex, search_value):
        queue = Queue()
        visited_vertices = {}
        visited_vertices[starting_vertex.value] = True
        queue.enqueue(starting_vertex)
        while queue.read():
            current_vertex = queue.dequeue()
            if current_vertex.value == search_value:
                return current_vertex
            for adjacent_vertex in current_vertex.adjacent_vertices:
                if adjacent_vertex.value not in visited_vertices:
                    visited_vertices[adjacent_vertex.value] = True
                    queue.enqueue(adjacent_vertex)
        return None


if __name__ == "__main__":
    # Create the vertices
    alice = Vertex("Alice")
    bob = Vertex("Bob")
    candy = Vertex("Candy")
    derek = Vertex("Derek")
    elaine = Vertex("Elaine")
    fred = Vertex("Fred")
    gina = Vertex("Gina")
    helen = Vertex("Helen")
    irena = Vertex("Irena")

    # Add the edges
    alice.add_adjacent_vertex(bob)  # alice: [bob] => bob: [alice]
    alice.add_adjacent_vertex(candy)
    alice.add_adjacent_vertex(derek)
    alice.add_adjacent_vertex(elaine)
    bob.add_adjacent_vertex(fred)
    fred.add_adjacent_vertex(helen)
    helen.add_adjacent_vertex(candy)
    derek.add_adjacent_vertex(gina)
    derek.add_adjacent_vertex(elaine)
    gina.add_adjacent_vertex(irena)

    # vertices = [alice, bob, candy, derek, elaine, fred, gina, helen, irena]
    # for vertex in vertices:
    #     print(f"Adjacent vertices for {vertex.value}: ")
    #     vertex.print_adjacent_vertices()

    graph = Graph()

    # Test the depth-first search traversal
    print("Depth-first search traversal:")
    graph.dfs_traverse(alice)

    # Test the depth-first search
    print("Depth-first search:")
    print(graph.dfs(alice, "Irena").value)

    # Test the breadth-first search traversal
    print("Breadth-first search traversal:")
    graph.bfs_traverse(alice)

    # Test the breadth-first search
    print("Breadth-first search:")
    print(graph.bfs(alice, "Irena").value)
