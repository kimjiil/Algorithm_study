#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

int main()
{
	cin.tie(NULL)->sync_with_stdio(false);
	int N, M;
	cin >> N >> M;

	vector<vector<int>> v;
	vector<int> v_r;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int a;
			cin >> a;
			v_r.push_back(a);
		}
		v.push_back(v_r);
		v_r.clear();
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int a;
			cin >> a;
			cout << v[i][j] + a << " ";
		}
		cout << "\n";
	}
}