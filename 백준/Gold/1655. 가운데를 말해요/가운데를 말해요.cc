#include <iostream>
#include <queue>
using namespace std;

int main()
{
	cin.tie(NULL)->sync_with_stdio(false);

	int n;

	cin >> n;
	priority_queue<int, vector<int>, greater<int>> right_min_q;
	priority_queue<int, vector<int>, less<int>> left_max_q;

	int v;
	for (int i = 0; i < n; i++) {
		cin >> v;
		/*left_max_q.emplace(v);
		while (left_max_q.size() - right_min_q.size() >= 2) {
			int _top = left_max_q.top();
			left_max_q.pop();
			right_min_q.emplace(_top);
		}*/
		if (left_max_q.size() == 0) {
			left_max_q.emplace(v);
		}
		else if (left_max_q.top() >= v) {
			if (left_max_q.size() <= right_min_q.size()) {
				left_max_q.emplace(v);
			}
			else {
				left_max_q.emplace(v);
				right_min_q.emplace(left_max_q.top());
				left_max_q.pop();
			}
		}
		else {
			if (right_min_q.size() < left_max_q.size()) {
				right_min_q.emplace(v);
			}
			else {
				right_min_q.emplace(v);
				left_max_q.emplace(right_min_q.top());
				right_min_q.pop();
			}
		}

		std::cout << left_max_q.top() << "\n";
	}

	return 0;
}