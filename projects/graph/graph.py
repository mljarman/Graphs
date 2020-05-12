"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        # keep track of visited nodes
        visited = set()
        # repeat until queue is empty
        while q.size() > 0:
            # dequeue first vert
            v = q.dequeue()
            # if its not visited:
            if v not in visited:
                # mark as visited
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
        [print(v) for v in visited]

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        # keep track of visited nodes
        visited = set()
        # repeat until queue is empty
        while s.size() > 0:
            # dequeue first vert
            v = s.pop()
            # if its not visited:
            if v not in visited:
                # mark as visited
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
            *explore*:
                print this node
                *explore* all its unvisited neighbors
                return
        """
        print(starting_vertex)
        # create the set:
        if visited is None:
            visited = set()
        # add starting vertex to visited
        visited.add(starting_vertex)

        for next_vert in self.vertices[starting_vertex]:
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            current_path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = current_path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
            # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
              # IF SO, RETURN PATH
                    return current_path
                # Mark it as visited...
                visited.add(last_vertex)
            # Then add A PATH TO its neighbors to the back of the queue
                for next_vert in self.get_neighbors(last_vertex):
                    q.enqueue(current_path + [next_vert])


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first PATH
            current_path = s.pop()
            # Grab the last vertex from the PATH
            last_vertex = current_path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
            # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
              # IF SO, RETURN PATH
                    return current_path
                # Mark it as visited...
                visited.add(last_vertex)
            # Then add A PATH TO its neighbors to the back of the queue
                for next_vert in self.get_neighbors(last_vertex):
                    s.push(current_path + [next_vert])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # create visited set and path list:
        if visited is None:
            visited = set()

        if path is None:
            path =[]
        # add starting vertex to visited:
        visited.add(starting_vertex)
        #make a copy of the lists, adding the new vertex on
        path = path + [starting_vertex]

        #base case, finding target:
        if starting_vertex == destination_vertex:
            return path
        # otherwise, search through graph looking for target:
        for next_vert in self.vertices[starting_vertex]:
            if next_vert not in visited:
                new_path = self.dfs_recursive(next_vert, destination_vertex, visited, path)

                if new_path:
                    return new_path
        # if target not in graph, return none.
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
    print(graph.vertices)

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
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
