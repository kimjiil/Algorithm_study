#include <iostream>
#include <stdlib.h>

using namespace std;


int main()
{
	cin.tie(NULL)->sync_with_stdio(false);
	int n;
	cin >> n;
	int a, b;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		cout << a + b << "\n";
	}
}