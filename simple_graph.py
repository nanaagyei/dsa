from data_structures_algos.stack_queues import Queue  # Import Queue class from stack_queues module

# Vertex class for the graph


class Vertex:  # Define a class Vertex

    # Initialize the vertex with a value and an empty list of adjacent vertices
    def __init__(self, value):  # Constructor for Vertex class
        self.value = value  # Assign the value to the vertex
        self.adjacent_vertices = []  # Initialize an empty list for adjacent vertices

    # Add an adjacent vertex to the vertex's list of adjacent vertices
    def add_adjacent_vertex(self, vertex):  # Method to add an adjacent vertex
        if vertex in self.adjacent_vertices:  # Check if the vertex is already in the list
            return  # If yes, return without adding
        self.adjacent_vertices.append(vertex)  # Add the vertex to the list
        # Add this vertex to the adjacent vertex's list
        vertex.add_adjacent_vertex(self)

    # Print adjacent vertices for a particular vertex
    def print_adjacent_vertices(self):  # Method to print adjacent vertices
        for vertex in self.adjacent_vertices:  # Loop through the list of adjacent vertices
            print(vertex.value)  # Print the value of each vertex


class Graph:  # Define a class Graph

    # Depth-first search traversal
    def dfs_traverse(self, vertex, visited_vertices={}):  # Method for DFS traversal
        visited_vertices[vertex.value] = True  # Mark the vertex as visited
        print(vertex.value)  # Print the value of the vertex
        for adjacent_vertex in vertex.adjacent_vertices:  # Loop through the adjacent vertices
            # If the vertex is visited, skip
            if visited_vertices.get(adjacent_vertex.value, False):
                continue
            # Recursively call the method for the adjacent vertex
            self.dfs_traverse(adjacent_vertex, visited_vertices)

    # Depth-first search
    def dfs(self, vertex, search_value, visited_vertices={}):  # Method for DFS
        if vertex.value == search_value:  # If the vertex value is the search value, return the vertex
            return vertex
        visited_vertices[vertex.value] = True  # Mark the vertex as visited
        for adjacent_vertex in vertex.adjacent_vertices:  # Loop through the adjacent vertices
            # If the vertex is visited, skip
            if visited_vertices.get(adjacent_vertex.value, False):
                continue
            # If the adjacent vertex value is the search value, return the vertex
            if adjacent_vertex.value == search_value:
                return adjacent_vertex
            vertex_were_searching_for = self.dfs(  # Recursively call the method for the adjacent vertex
                adjacent_vertex, search_value, visited_vertices)
            if vertex_were_searching_for:  # If the vertex is found, return it
                return vertex_were_searching_for
        return None  # If the vertex is not found, return None

    # Breadth-first search traversal
    def bfs_traverse(self, starting_vertex):  # Method for BFS traversal
        queue = Queue()  # Initialize a queue
        visited_vertices = {}  # Initialize a dictionary for visited vertices
        # Mark the starting vertex as visited
        visited_vertices[starting_vertex.value] = True
        queue.enqueue(starting_vertex)  # Enqueue the starting vertex
        while queue.read():  # While the queue is not empty
            current_vertex = queue.dequeue()  # Dequeue a vertex
            print(current_vertex.value)  # Print the value of the vertex
            for adjacent_vertex in current_vertex.adjacent_vertices:  # Loop through the adjacent vertices
                if adjacent_vertex.value not in visited_vertices:  # If the vertex is not visited
                    # Mark the vertex as visited
                    visited_vertices[adjacent_vertex.value] = True
                    queue.enqueue(adjacent_vertex)  # Enqueue the vertex

    # Breadth-first search
    def bfs(self, starting_vertex, search_value):  # Method for BFS
        queue = Queue()  # Initialize a queue
        visited_vertices = {}  # Initialize a dictionary for visited vertices
        # Mark the starting vertex as visited
        visited_vertices[starting_vertex.value] = True
        queue.enqueue(starting_vertex)  # Enqueue the starting vertex
        while queue.read():  # While the queue is not empty
            current_vertex = queue.dequeue()  # Dequeue a vertex
            if current_vertex.value == search_value:  # If the vertex value is the search value, return the vertex
                return current_vertex
            for adjacent_vertex in current_vertex.adjacent_vertices:  # Loop through the adjacent vertices
                if adjacent_vertex.value not in visited_vertices:  # If the vertex is not visited
                    # Mark the vertex as visited
                    visited_vertices[adjacent_vertex.value] = True
                    queue.enqueue(adjacent_vertex)  # Enqueue the vertex
        return None  # If the vertex is not found, return None```


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
