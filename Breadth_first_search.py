from collections import deque
graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    print("BFS traversal order:")
    while queue:
        vertex=queue.popleft()
        if vertex not in visited:
          print(vertex)
          visited.add(vertex)
          queue.extend(graph[vertex])
bfs(graph,'A')
