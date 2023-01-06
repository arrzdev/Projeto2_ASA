#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
typedef tuple<int, int, int> Edge;

// disable sync with stdio for faster cin/cout
static const auto io_speed_up = []()
{ std::ios::sync_with_stdio(false); std::cin.tie(0); return 0; }();

int getRoot(vector<int> &parent, int vertex)
{
  int vertex_parent = parent[vertex];
  if (vertex_parent != vertex)
    // update parent so that we don't have to traverse again in the future
    // this is a memoization technique (pattern compression)
    parent[vertex] = getRoot(parent, vertex_parent);
  return parent[vertex];
}

void unionn(vector<int> &parent, vector<int> &rank, int u, int v)
{
  // implementation of union using ranking technique to keep the tree as
  // balanced as possible
  int x_root = getRoot(parent, u);
  int y_root = getRoot(parent, v);

  if (rank[x_root] < rank[y_root])
    parent[x_root] = y_root;
  else if (rank[x_root] > rank[y_root])
    parent[y_root] = x_root;
  else
  {
    parent[y_root] = x_root;
    rank[x_root]++;
  }
}

bool edgeSort(Edge e1, Edge e2)
{
  return get<2>(e1) > get<2>(e2);
}

int algo(vector<Edge> edges, int nvertices)
{
  // sort edges based on weight in descending order
  sort(edges.begin(), edges.end(), edgeSort);

  vector<int> parent(nvertices + 1);
  for (int i = 1; i <= nvertices; i++)
    parent[i] = i;
  vector<int> rank(nvertices + 1, 0);

  int total_trades = 0;
  for (Edge edge : edges)
  {
    int u = get<0>(edge), v = get<1>(edge), w = get<2>(edge);
    if (getRoot(parent, u) != getRoot(parent, v)) // doesn't form a cycle
    {
      total_trades += w;
      unionn(parent, rank, u, v);
    }
  }

  return total_trades;
}

int main()
{
  int nvertices, nedges;
  cin >> nvertices >> nedges;

  vector<Edge> edges(nedges);
  for (int i = 0; i < nedges; i++)
  {
    int u, v, w;
    cin >> u >> v >> w;
    edges.emplace_back(u, v, w);
  }

  cout << algo(edges, nvertices) << endl;
  return 0;
}