from typing import List, Tuple
import heapq

class DisjointSet:
  def __init__(self, n: int):
    self.parent = {i: i for i in range(n + 1)}

  def find(self, x: int) -> int:
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x: int, y: int) -> None:
    xroot = self.find(x)
    yroot = self.find(y)
    if xroot == yroot:
      return
    self.parent[xroot] = yroot

def prj(edges: List[Tuple[int, int, int]], vertices: int) -> int:
  ds = DisjointSet(vertices)
  heap = [(w, u, v) for u, v, w in edges]
  heapq.heapify(heap)

  count = 0
  while heap:
    w, u, v = heapq.heappop(heap)
    if ds.find(u) != ds.find(v):
      count += w
      ds.union(u, v)

  return count

def main():
  vertices = int(input())

  edges = []
  for _ in range(int(input())):
    edges.append(tuple(map(int, input().split())))

  print(prj(edges, vertices))
