#include <iostream>
#include <queue>

using namespace std;

int V, E;
int* vertex;

struct edge {
	int weight;
	int v1, v2;

	edge(int v1, int v2, int weight) : v1(v1), v2(v2), weight(weight) {}
};

bool operator>(const edge& e1, const edge& e2) {
	return e1.weight > e2.weight;
}

int find_parent(int v) {
	while (vertex[v] != v) {
		v = vertex[v];
	}
	return v;
}

bool cycle(edge e) {

	int v1_p = find_parent(e.v1);
	int v2_p = find_parent(e.v2);

	if (v1_p != v2_p) { // 부모가 같지 않으면 서로 다른 트리에 속해있음.
		return false;
	}
	return true;
}

void union_tree(edge e) {
	int v1_p = find_parent(e.v1);
	int v2_p = find_parent(e.v2);

	vertex[v2_p] = e.v1;
}

int main()
{
	cin.tie(NULL)->sync_with_stdio(false);

	cin >> V >> E;
	vertex = new int[V];
	for (int v = 0; v < V; v++) {
		vertex[v] = v;
	}

	priority_queue<edge, vector<edge>, greater<edge> > pq; //최소힙

	for (int e = 0; e < E; e++) {
		int a, b, w;
		cin >> a >> b >> w;

		pq.push(edge(a - 1, b - 1, w));
	}

	int total_weight = 0;
	while (!pq.empty()) {
		edge cur = pq.top();
		pq.pop();

		// a, b의 간선이 추가됨으로써 사이클이 형성되지 않으면 추가함
		if (!cycle(cur)) {
			union_tree(cur);
			total_weight += cur.weight;
		}
	}

	cout << total_weight;
	return 0;
}