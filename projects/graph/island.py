# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]


# island_counter(islands) # returns 4

# islands consist of - connected components:
# connected - neighbors (edges)
# directions, NESW (edges)
# 2D Array - raph, more or less?
# Returns (shape of solution) - number of islands

# How could we write a get_neighbor function that uses this shape?
# You would offset coordinates

# How can we find the extent of an island?
# Either of our traversals to find all of the nodes in an island

# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1


n = 4
# n2 = 4
a = [[0] * n for i in range(n)]
# b = [[0] * n2 for i in range(n2)]

for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
            
            
# for i in range(n2):
#     for j in range(0, i):
#         b[i][j] = 2
#     b[i][j] = 1
#     for j in range(i + 1, n2):
#         b[i][j] = 0
        
n2 = 4
b = [[0] * n for i in range(n2)]

for i in range(n2):
    for j in range(0, i):
        b[i][j] = 2
    b[i][i] = 1
    for j in range(i + 1, n2):
        b[i][j] = 0


        
for row in a:
    print(' '.join([str(element) for element in row]))

print('===-==-================')

for row in b:
    print(' '.join([str(elem) for elem in row]))