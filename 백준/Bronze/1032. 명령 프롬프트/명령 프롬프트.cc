#include <iostream>
#include <string.h>
#include <vector>
using namespace std;

int main() {
	cin.tie(NULL)->sync_with_stdio(false);

	int n;
	cin >> n;

	vector<string> s_v;
	string s;
	int s_l;
	for (int i = 0; i < n; i++) {
		cin >> s;
		s_v.push_back(s);
		s_l = s.size();
	}
	
	vector<char> c;

	for (int i = 0; i < s_l; i++) {
		char a = s_v[0][i];
		bool isequal = true;
		for (int j = 1; j < s_v.size(); j++) {
			if (a != s_v[j][i]) {
				isequal = false;
			}
		}

		if (isequal) {
			c.push_back(a);
		}
		else {
			c.push_back('?');
		}
	}

	string ss(c.begin(), c.end());
	cout << ss;
}