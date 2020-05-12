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
'''
How to solve any graph problem
1. translate the problem into graph terminology
2. build the graph
3. traverse it

Word Ladder problem
--------------------

begin: hit
end: cog

hit -> hot -> cot -> cog

begin: sail
end boat

sail -> bail -> tail -
'''

#     def find_ladders(begin_word, end_word):
#         visited = set()
#         q = Queue()
#
#         q.enqueue([begin_word])
#
#         while q.size() > 0:
#             path = q.dequeue()
#
#             v = path[-1]
#
#             if v not in visited:
#                 visited.add(v)
#                 # Did we reach the end word?
#                 if v == end_word:
#                     return path
#                 for neighbor in get_neighbors(v):
#                     path_copy = list(path)
#                     path_copy.append(neighbor)
#
#                     q.enqueue(path_copy)
# with open('words.txt') as f:
#     words = f.read().split()
#
# word_set = set()
#
# for w in words:
#     word_set.add(w.lower())
# letters = list(string_ascii_lowercase)
# def get_neighbors_w(word):
#     # return this:
#     neighbors = []
#     string_word = list(word) # [ 'w', 'o', 'r', 'd']
#
#     # for each letter...
#     for i in range(len(string_word)):
#         for letter in letters:
#             # make a copy of the word so we can munge it
#             temp_word = list(string_word)
#             temp_word[i] = letter # change into a new candidate word
#             w = "".join(temp_word)
#             # if its a valid word, add it to neighbors
#             if w != word and w in word_set:
#                 neighbors.append(w)
#     return neighbors
