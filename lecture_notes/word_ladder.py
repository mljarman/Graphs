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

    def find_ladders(begin_word, end_word):
        visited = set()
        q = Queue()

        q.enqueue([begin_word])

        while q.size() > 0:
            path = q.dequeue()

            v = path[-1]

            if v not in visited:
                visited.add(v)
                # Did we reach the end word?
                if v == end_word:
                    return path
                for neighbor in get_neighbors(v):
                    path_copy = list(path)
                    path_copy.append(neighbor)

                    q.enqueue(path_copy)
with open('words.txt') as f:
    words = f.read().split()

word_set = set()

for w in words:
    word_set.add(w.lower())
letters = list(string_ascii_lowercase)
def get_neighbors_w(word):
    # return this:
    neighbors = []
    string_word = list(word) # [ 'w', 'o', 'r', 'd']

    # for each letter...
    for i in range(len(string_word)):
        for letter in letters:
            # make a copy of the word so we can munge it
            temp_word = list(string_word)
            temp_word[i] = letter # change into a new candidate word
            w = "".join(temp_word)
            # if its a valid word, add it to neighbors
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors
