from queue import Queue
from graph import Graph

# First we need to create a graph using the collection we're given
def create_graph_from(ancestors):
    # create a graph instance
    g = Graph()
    
    # Loop through all pairs in ancestors
    # Note: In the Graph class `add_vertex` checks...
    # ..to make sure the vertex hasn't already been added yet.
    # Then we add the edges (relationships)
    # Lastly, we return the graph so we can traverse it.
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        g.add_vertex(parent)
        g.add_vertex(child)
                   
        g.add_edge(child, parent)
        
    return g 


def earliest_ancestor(ancestors, starting_node):
    # Create an instance of the new graph
    g = create_graph_from(ancestors)
    
    # We simply use our bft function which...
    # ...will return the earliest ancestor or a -1
    return g.bft(starting_node)
