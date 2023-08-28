#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	cin.tie(NULL)->sync_with_stdio(false);

	string a;
	cin >> a;
	for (int i = 0; i < a.size(); i++) {
		if ('A' <= a[i] && a[i] <= 'Z') {
			a[i] += 32;
		}
		else {
			a[i] -= 32;
		}
	}
	cout << a << "\n";
}