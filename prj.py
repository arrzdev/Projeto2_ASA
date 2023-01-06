def find(parent, vertex):
  if parent[vertex] != vertex:
    parent[vertex] = find(parent, parent[vertex])
  return parent[vertex]

def union(parent, u, v):
  xroot = find(parent, u)
  yroot = find(parent, v)
  parent[xroot] = yroot

def prj(edges, vertices):
  edges.sort(key=lambda x: x[2], reverse=True)

  parent = [i for i in range(vertices+1)]

  total_transactions = 0
  for edge in edges:
    u, v, w = edge
    if find(parent, u) != find(parent, v):
      total_transactions += w
      union(parent, u, v)

  return total_transactions

def main():
  vertices = int(input())

  edges = []
  for _ in range(int(input())):
    edges.append(tuple(map(int, input().split())))

  print(prj(edges, vertices))

if __name__ == '__main__':
  main()