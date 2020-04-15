from queue import Queue
from graph import Graph

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    # '''
    #    10
    #  /
    # 1   2   4  11
    #  \ /   / \ /
    #   3   5   8
    #    \ / \   \
    #     6   7   9
    # '''

def helperGraph(ancestors):
    g = Graph()
    
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        g.add_vertex(parent)
        g.add_vertex(child)
                   
        g.add_edge(child, parent)
        
    return g 


def earliest_ancestor(ancestors, starting_node):
    g = helperGraph(ancestors)
    print(g.vertices)
    
    return g.bft(starting_node)

   
    
    
    