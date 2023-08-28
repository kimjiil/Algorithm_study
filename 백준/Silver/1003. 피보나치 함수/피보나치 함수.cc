
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;



int main() {
	cin.tie(NULL)->sync_with_stdio(false);
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		if (a == 0) {
			cout << "1 0\n";
		}
		else {
			int n1, n2;
			n1 = 0;
			n2 = 1;
			int temp;
			while (a > 1) {
				temp = n2;
				n2 = n1 + n2;
				n1 = temp;
				a--;
			}
			cout << n1 << " " << n2 << "\n";
		}
	}
}