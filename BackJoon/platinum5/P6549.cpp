#include <iostream>
#include <stack>

using namespace std;

#define ULL unsigned long long int

struct point {
	int idx;
	int h;
	point(ULL h, int idx) : idx(idx), h(h) {};

};

bool operator>(const point& p1, const point& p2) {
	if (p1.h > p2.h) {
		return true;
	}
	return false;
}

bool operator<(const point& p1, const point& p2) {
	if (p2.h > p1.h) {
		return true;
	}
	return false;
}

bool operator>=(const point& p1, const point& p2) {
	if (p1.h >= p2.h) {
		return true;
	}
	return false;
}

bool operator<=(const point& p1, const point& p2) {
	if (p1.h <= p2.h) {
		return true;
	}
	return false;
}


ULL solution(int* rec_list, int n) {

	stack<point> st;
	st.push(point(-1, -1)); // (h, idx)

	ULL max_rect = 0;
	for (int i = 0; i < n; i++) {
		point cur(rec_list[i], i);
		if (st.top() <= cur) {
			st.push(cur);
		}
		else {
			ULL rect_s;
			int last_idx = i;
			int cur_idx;
			while (st.top() >= cur) {
				cur_idx = st.top().idx;
				rect_s = static_cast<ULL>(st.top().h) * static_cast<ULL>(last_idx - cur_idx);
				if (max_rect < rect_s) {
					max_rect = rect_s;
				}
				st.pop();
			}
			st.push(point(cur.h, cur_idx));
		}
	}
	return max_rect;
}

int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	while (true) {
		int n;
		cin >> n;

		if (n == 0) {
			return 0;
		}

		int* rec_list = new int[n + 1];

		for (int i = 0; i < n; i++) {
			cin >> rec_list[i];
		}
		rec_list[n] = 0;

		cout << solution(rec_list, n + 1) << "\n";
	}

	return 0;
}