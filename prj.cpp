#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
typedef tuple<int, int, int> Edge;

static const auto io_speed_up = []()
{ std::ios::sync_with_stdio(false); std::cin.tie(0); return 0; }();

int find(vector<int> &parent, int x)
{
  if (parent[x] != x)
    parent[x] = find(parent, parent[x]);
  return parent[x];
}

void unionn(vector<int> &parent, int x, int y)
{
  int xroot = find(parent, x);
  int yroot = find(parent, y);
  parent[xroot] = yroot;
}

bool edgeSort(Edge e1, Edge e2)
{
  return get<2>(e1) > get<2>(e2);
}

int algo(vector<Edge> edges, int nvertices)
{
  // sort edges based on weight in descending order
  sort(edges.begin(), edges.end(), edgeSort);

  // init parent vector
  vector<int> parent(nvertices);
  for (int i = 1; i <= nvertices; i++)
    parent[i] = i;

  int total_weight = 0;
  for (Edge edge : edges)
  {
    int u = get<0>(edge), v = get<1>(edge), w = get<2>(edge);
    if (find(parent, u) != find(parent, v))
    {
      total_weight += w;
      unionn(parent, u, v);
    }
  }

  return total_weight;
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