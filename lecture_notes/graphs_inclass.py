class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vert_id):
        self.vertices[vertex_id] = set() # set of edges

    def add_edge(self, v1, v2):
        """Add edge from v1 to v2"""
        # if they're both in the graph:
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError('Vertex does not exist in graph')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

g = Graph()
g.add_vertex(99)
g.add_vertex(3)
g.add_vertex(3490)
g.add_edge(99, 3) # connect node 99 to node 3
g.add_edge(99, 3490) # connect node 99 to node 3490
g.add_edge(3, 99) # connect node 3 to node 99 (undirected)

g.get_neighors(99)

'''
breadth first traversal

1. add starting node to a queue
2. while queue isn't empty:
    dequeue the first vert
    if that vert isn't visited:
        mark as visited
        add all its unvisited neighbors to the queue
'''
def bft(self, starting_vertex_id):
    q = Queue()
    q.enqueue(starting_vertex_id)

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
'''
depth first

add starting node to a stack

while stack isn't empty:
    pop the first vert
    if that vert isn't visited:
        mark as visited
        push all its unvisited neighbors to stack
        use recursion since its a stack
        '''
