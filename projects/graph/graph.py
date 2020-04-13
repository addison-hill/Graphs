"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack push the starting vortex
        # create a set to store visited vertices
        # while the stack is not empty
        # pop the first vortex
        # check if its been visited
        # if it hasnt been visited...
        # mark it as visited
        # push all its neighbors onto the stack

        ss = Stack()
        ss.push(starting_vertex)
        visited = set()

        while ss.size() > 0:
            v = ss.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    ss.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # check if the node has been visited
        # if not...
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
            print(starting_vertex)
            # Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        qq = Queue()
        # Enqueue A PATH TO the starting vertex
        qq.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while qq.size() > 0:
            # Dequeue the first Path
            path = qq.dequeue()
            # Grab the vertex from the end of the path
            v = path[-1]
            # check if its been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Check if its the target
                if v == destination_vertex:
                    # If so, return the path
                    return path
                # Enqueue a path to all its neighbors
                for neighbor in self.get_neighbors(v):
                    # Make a copy of the path
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # enqueue the copy
                    qq.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        ss = Stack()
        # push A PATH TO the starting vertex
        ss.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while ss.size() > 0:
            # pop the first Path
            path = ss.pop()
            # Grab the vertex from the end of the path
            v = path[-1]
            # check if its been visited
            # If it hasn't been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Check if its the target
                if v == destination_vertex:
                    # If so, return the path
                    return path
                # push a path to all its neighbors
                for neighbor in self.get_neighbors(v):
                    # Make a copy of the path
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # push the copy
                    ss.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
