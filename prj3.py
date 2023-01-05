def algo(edges, vertices):
  edges.sort(key=lambda x: x[2], reverse=True)
  uf = UnionFind(vertices)
  max_w = 0
  for edge in edges:
    u, v, w = edge
    if uf.find(u) != uf.find(v):
      max_w += w
      uf.union(u, v)

  #get the sum of the weights of the edges in the path
  return max_w

class UnionFind:
  def __init__(self, vertices):
    self.parent = {}
    #init parents
    for vertex in vertices:
      self.parent[vertex] = vertex

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    xroot = self.find(x)
    yroot = self.find(y)
    if xroot == yroot:
      return
    self.parent[xroot] = yroot

def read_input():
  vertices = [i for i in range(1, int(input())+1)]
  
  edges = []
  for _ in range(int(input())):
    edges.append(tuple(map(int, input().split())))

  #run algo
  print(algo(edges, vertices))
  

if __name__ == "__main__":
  read_input()