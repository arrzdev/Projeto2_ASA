#so given a graph with E edges and V vertices where each edge has a weight (profit)
#we want to find the path that maximizes the profit but minimizes the number of edges

#we can use a greedy algorithm to solve this problem
#we can sort the edges by weight and then add them to the path if they don't create a cycle
#we can use a union find data structure to check if adding an edge creates a cycle

def prj(edges, vertices):
  edges.sort(key=lambda x: x[2], reverse=True)
  uf = UnionFind(vertices)
  path = []
  for edge in edges:
    u, v, _ = edge
    if not uf.find(u, v):
      path.append(edge)
      uf.union(u, v)

  #get the sum of the weights of the edges in the path
  return sum([edge[2] for edge in path])

class UnionFind:
  def __init__(self, vertices):
    self.parent = {}
    self.rank = {}
    for vertex in vertices:
      self.parent[vertex] = vertex
      self.rank[vertex] = 0

  def find(self, x, y):
    return self.find_helper(x) == self.find_helper(y)

  def find_helper(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find_helper(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    xroot = self.find_helper(x)
    yroot = self.find_helper(y)
    if self.rank[xroot] < self.rank[yroot]:
      self.parent[xroot] = yroot
    elif self.rank[xroot] > self.rank[yroot]:
      self.parent[yroot] = xroot
    else:
      self.parent[yroot] = xroot
      self.rank[xroot] += 1

if __name__ == "__main__":
  vertices = [i for i in range(1, int(input())+1)]
  
  edges = []
  for _ in range(int(input())):
    edges.append(tuple(map(int, input().split())))

  print(prj(edges, vertices))