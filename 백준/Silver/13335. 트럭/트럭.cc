#include <iostream>
#include <queue>;

using namespace std;

struct block {
	int weight, num;

	block(int weight, int num) : weight(weight), num(num) {

	}
};

int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	// n 다리를 건너는 트럭수
	// w 다리의 길이
	// l 다리의 최대 하중
	int n, w, l;
	cin >> n >> w >> l;

	int* truck = new int[n];
	int* t = new int[n];
	int time = 1;
	int cur_l = 0;
	queue<int> bridge;
	for (int i = 0; i < w; i++) {
		bridge.push(0);
	}
	for (int i = 0; i < n; i++) {
		cin >> truck[i];
		// 처음 다리에 들어가는 경우

		int front_q = bridge.front();
		bridge.pop();

		if (front_q != 0) {
			cur_l -= front_q;
		}

		if (cur_l + truck[i] <= l) {
			bridge.push(truck[i]);
			cur_l += truck[i];
		}
		else if (cur_l + truck[i] > l) {
			cur_l += truck[i];

			while (cur_l > l) {
				int t_q = bridge.front();
				bridge.pop();
				if (t_q != 0) {
					cur_l -= t_q;
				}
				bridge.push(0);

				time++;
			}
			bridge.push(truck[i]);
		}
		time++;
	}
	
	cout << time + w - 1;

	return 0;
}