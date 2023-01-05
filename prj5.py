from typing import List, Tuple

def find(parent: List[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent: List[int], x: int, y: int) -> None:
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot == yroot:
      return
    parent[xroot] = yroot

def prj(edges: List[Tuple[int, int, int]], vertices: int) -> int:
    edges.sort(key=lambda x: x[2], reverse=True)

    parent = [i for i in range(vertices + 1)]

    count = 0
    for edge in edges:
        u, v, w = edge
        if find(parent, u) != find(parent, v):
            count += w
            union(parent, u, v)

    return count

def main():
    vertices = int(input())

    edges = []
    for _ in range(int(input())):
      edges.append(tuple(map(int, input().split())))

    print(prj(edges, vertices))

if __name__ == '__main__':
    main()
