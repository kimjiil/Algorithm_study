#include <iostream>

using namespace std;

#define ull unsigned long long int

int main() {
	cin.tie(NULL)->sync_with_stdio(false);
	int N, B, C;
	int A[1000000];
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}

	cin >> B >> C;
	ull com = 0;
	for (int i = 0; i < N; i++) {
		//A[i] = A[i] - B;
		com++;
		if (A[i] - B > 0) {
			com += ((A[i] - B) / C);
			if ((A[i] - B) % C > 0) {
				com++;
			}
		}
	}

	cout << com << "\n";
	return 0;
}