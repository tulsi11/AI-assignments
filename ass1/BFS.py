from queue import Queue

def BFS(graph, start_node, target_node):
    # Set of visited nodes to prevent loops
    visited = set()
    queue = Queue()

    # Add the start_node to the queue and visited list
    queue.put(start_node)
    visited.add(start_node)
    
    # start_node has not parents
    parent = dict()
    parent[start_node] = None

    # Perform step 3
    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == target_node:
            path_found = True
            break

        for next_node in graph[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)
                
    # Path reconstruction
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node]) 
            target_node = parent[target_node]
        path.reverse()
    return path
    
graph = {
  0 : [1, 7],
  1 : [0, 7, 2],
  7 : [0, 1, 8, 6],
  2 : [1, 8, 3, 5],
  8 : [7, 6],
  6 : [7, 8, 5],
  5 : [2, 3, 4, 6],
  3 : [2, 4, 5],
  4 : [3, 5]
}
path = BFS(graph, 0, 5)
print(path)