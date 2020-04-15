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
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2.
        """
        # Check if they exist first
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print("Error adding edge: Vertex not found")

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
        # Create a queue and enqueue starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        
        # Create a set of traversed vertices
        visited = set()
        # Creates a different path so we can compare lengths with path (line 55)
        # The longest path will be set to ancestor path, which is the one we're looking for
        ancestor_path = [starting_vertex]
        
        # Only want to continue if the queue isn't empty
        while queue.size() > 0:
            # dequeue/pop first path
            path = queue.dequeue()
            # Grab the last node from path
            node = path[-1]
            
            # Only if the node has not been visited:
            if node not in visited:
                # DO THE THING -> comparing path lengths (we want the longest one)
                if len(path) > len(ancestor_path):
                    ancestor_path = path
                # If the lengths of both the path and ancestor path are the same, 
                # then we compare the last element of each path, going with the smallest
                elif len(path) == len(ancestor_path):
                    if path[-1] < ancestor_path[-1]:
                        ancestor_path = path
                    # No else. If the last element of path is not smaller,
                    # then the path aready asigned to ancestor_path stays the same
                    
                # Mark the node as visited
                visited.add(node)
                
                # Enqueue all neighbors
                for next_vert in self.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
        
        # per assignment requirements, we need to return the earliest ancestor
        # If some paths don't have any more ancestors, we return -1, otherwise return
        # the last element in ancestor_path
        if len(ancestor_path) == 1:
            return -1
        else:
            return ancestor_path[-1]

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack and push starting_vertex onto stack
        stack = Stack()
        stack.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # while stack is not empty:
        while stack.size() > 0:
            # Pop last vertex
            path = stack.pop()
            topNode = path[-1]
            
            if topNode not in visited:
                # DO THE THING
                print(topNode)
                # Mark as visited
                visited.add(topNode)
                # Enqueue all neighbors
                for next_vert in self.get_neighbors(topNode):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initial case
        if visited is None:
            visited = set()
        # Base case: How do we know we're done?
        # We're done when we have no more neighbors
        
        # Track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)
        
        # Call the function recursively - on neighbors Not Visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)
                # If a node has no unvisited neighbors <- This is our base case!

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        # Create a queue and enqueue starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while queue.size() > 0:
            # dequeue/pop first vertex
            path = queue.dequeue()
            node = path[-1]
            # if not visited
            if node not in visited:
                # DO THE THING
                if node == destination_vertex:
                    return path
                # Mark as visited
                visited.add(node)
                # Enqueue all neighbors
                for next_vert in self.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack and push starting_vertex onto stack
        stack = Stack()
        stack.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # while stack is not empty:
        while stack.size() > 0:
            # Pop last vertex
            path = stack.pop()
            topNode = path[-1]
            
            if topNode not in visited:
                # DO THE THING
                if topNode == destination_vertex:
                    return path
                # Mark as visited
                visited.add(topNode)
                # Enqueue all neighbors
                for next_vert in self.get_neighbors(topNode):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initial case
        if visited is None:
            visited = set()
            
        if path is None:
            path = []
        # Base case: How do we know we're done?
        # We're done when we have no more neighbors
        
        # Track visited nodes
        visited.add(starting_vertex)
        newPath = path + [starting_vertex]
        
        # DO THE THING
        if starting_vertex == destination_vertex:
            return newPath
        
        # Call the function recursively - on neighbors Not Visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                neighborPath = self.dfs_recursive(neighbor, destination_vertex, visited, newPath)
                if neighborPath:
                    return neighborPath
                # If a node has no unvisited neighbors <- This is our base case!

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
