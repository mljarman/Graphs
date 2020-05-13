class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

island = [[0, 1, 0, 1, 0],
          [1, 1, 0, 1, 1],
          [0, 0, 1, 0, 0],
          [1, 0, 1, 0, 0],
          [1, 1, 0, 0, 0]]

def island_counter(matrix):
    ''' create a visited data structure
    # walk through all the nodes, elements in the input matrix
        # if not visited:
            #if its a 1:
                # do a traversal and mark each as visited
                # increment island counter '''
    visited = []
    # make duplicate sized matrix filled with falses
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    island_count = 0
    # walk through all the nodes, elements in the input matrix
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # if not visited:
            if not visited[row][col]:
                #if its a 1:
                if matrix[row][col] == 1:
                    # do a traversal and mark each as visited
                    visited = dft(row, col, matrix, visited)
                    island_count += 1
            else:
                # we hit water (0)
                visited[row][col] = True
    return island_count

def dft(row, col, matrix, visited):
    s = Stack()
    # push starting vert on the stack
    s.push((row,col))

    # while stack not empty
    while s.size() > 0:
        # pop the first vert
        v = s.pop()
        # extract the row column from tuple
        row, col = v
        # if not visited, traverse!
        if not visited[row][col]:
            # mark visited
            visited[row][col] = True

            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)
    return visited

def get_neighbors(row, col, matrix):
    neighbors = []

    # check north
    if row > 0 and matrix[row -1][col] == 1:
        neighbors.append((row-1, col))
    # check south
    if row < len(matrix) -1 and matrix[row + 1][col] == 1:
        neighbors.append((row+1, col))
    # check west
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append((row, col -1))
    # check east
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1))
    return neighbors

print(island_counter(island))
