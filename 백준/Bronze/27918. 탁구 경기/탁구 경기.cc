#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<char> v_c;
    char c;
    for (int i = 0; i < n; i++) {
        cin >> c;
        v_c.push_back(c);
    }
    
    int D = 0;
    int P = 0;
    for (int i = 0; i < n; i++) {
        if (v_c[i] == 'D') {
            D++;
        }
        else if (v_c[i] == 'P') {
            P++;
        }
        if (abs(D - P) >= 2) {
            printf("%d:%d\n", D, P);
            return 0;
        }
    }
    printf("%d:%d\n", D, P);
    return 0;
}