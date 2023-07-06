// title : 팔

#include <iostream>
#include <string>
using namespace std;

/*
  L,R이 주어지는데 1 <= L <= R <= 2,000,000,000 일때
  [L, R] 사이의 구간에서 8이 가장 적게 포함되어 있는 수를 return
  이 사이에 존재할수 있는 8은 최대
  1,888,888,888 => 9개
  1 => 최소 0개
  <1>
  8 18 28 38 48 58 68 78 98 108 118 128 138 148 158 ... 181 .. 187 189 ... 800 ... 807 809
  <2>
  88 188 288 388 ... 808 818 828 ... 880 881 882 ... 1880 ...

  18....에서 최대자릿수에 존재하는 8에서 가장 가까운 값은 190 ... 0 으로 변경했을때 그 값이 최대값을 넘지 않으면
  8의 개수가 변화한다.

*/
int str_count(string s) {
	int c_n = 0;
	for (char& c : s) {
		if (c == '8') {
			c_n++;
		}
	}
	return c_n;
}
int main() {
	cin.tie(NULL)->sync_with_stdio(false);
	int L, R;
	cin >> L >> R;
	string int_L = to_string(L);
	int min_count = str_count(int_L);
	int s_l;
	string temp_str;
	if (min_count != 0) {
		s_l = int_L.size();

		for (int i = 0; i < s_l; i++) {
			if (int_L[i] == '8') {
				temp_str = int_L;
				temp_str[i] = '9';
				for (int j = i + 1; j < s_l; j++) {
					temp_str[j] = '0';
				}
				// 변경된 값이
				if (stoi(temp_str) <= R) {
					min_count = str_count(temp_str);
					break;
				}
			}
		}
	}
	cout << min_count << "\n";
}