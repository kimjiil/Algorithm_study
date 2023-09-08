#include <iostream>

using namespace std;
#define ull unsigned long long int

//18,446,744,073,709,551,615
// 4,611,686,014,132,420,609
// 2147483647
// 1805682608
ull a, b, c;
ull mypow(ull m, ull n) {

    if (n == 1) {
        return m % c;
    }
    else {
        ull temp = mypow(m, n / 2);
        if (n % 2 == 0) {
            return (temp * temp) % c;
        }
        else {
            ull t2 = (temp * temp) % c;
            return (t2 * m) % c;
        }
    }
}

int main()
{
    cin.tie(NULL)->sync_with_stdio(false);
    
    cin >> a >> b >> c;

    ull temp = mypow(a, b);

    cout << temp;
    return 0;
}