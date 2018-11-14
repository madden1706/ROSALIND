# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print("visited ", visited)
            stack.extend(graph[vertex] - visited)
            print("stack ", stack, "\n")
    return visited

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}