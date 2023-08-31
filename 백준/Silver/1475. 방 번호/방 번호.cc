#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;


int main()
{
	cin.tie(NULL)->sync_with_stdio(false);

	string room_no;

	cin >> room_no;

	int remain_set[9] = {0, }; // 0, 1,2,3,4,5,6,7,8,9 의 갯수

	for (int i = 0; i < room_no.length(); i++) {
		char c = room_no[i];

		int idx = c - 48;
		if (idx == 9) idx = 6;

		remain_set[idx]++;
	}

	remain_set[6] = int(ceil(float(remain_set[6]) / 2));

	int max_v = *max_element(remain_set, remain_set + 9);
	
	cout << max_v << "\n";
	return 0;

}