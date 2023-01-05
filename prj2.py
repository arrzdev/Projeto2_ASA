def maximize_profit(vertices, edges):
  # sort the edges by weight in non-decreasing order
  edges.sort(key=lambda x: x[2], reverse=True)

  uf = UnionFind(vertices)
  profit = 0
  for edge in edges:
    u, v, w = edge
    if not uf.find(u) == uf.find(v):
      profit += w
      uf.union(u, v)

  # get the sum of the weights of the edges in the path
  return profit

class UnionFind:
  def __init__(self, vertices):
    self.parent = {}
    self.rank = {}
    self.size = {}
    for vertex in vertices:
      self.parent[vertex] = vertex
      self.rank[vertex] = 0
      self.size[vertex] = 1

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    xroot = self.find(x)
    yroot = self.find(y)
    if xroot == yroot:
      return
    if self.rank[xroot] < self.rank[yroot]:
      xroot, yroot = yroot, xroot
    if self.rank[xroot] == self.rank[yroot]:
      self.rank[xroot] += 1
      
    self.parent[yroot] = xroot
    self.size[xroot] += self.size[yroot]


if __name__ == "__main__":
  vertices = [i for i in range(1, int(input())+1)]
  edges = []
  for _ in range(int(input())):
    edges.append(tuple(map(int, input().split())))

  print(maximize_profit(vertices, edges))
