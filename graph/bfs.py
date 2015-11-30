def bfs(graph, start_node):
    """
    Implement bfs on graph from start node.
    """
    start_node.distance = 0
    start.set_predecessor(None)
    queue = list()
    queue.append(start_node)
    while (len(queue) > 0):
        current_vertex = queue.pop()
        current_vertex.setState = "visiting"
        for vertex in current_vertex.links():
            if (vertex.getState == "unvisited"):
                vertex.setState == "tobevisited"
                vertex.set_predecessor(current_vertex)
                vertex.distance = current_vertex.distance + 1
                queue.append(vertex)
        current_vertex.setState = "visited"
