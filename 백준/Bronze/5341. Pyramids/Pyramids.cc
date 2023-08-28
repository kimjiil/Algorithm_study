#include <ios>

main()
{
    int n;
    while (true){
        scanf("%d", &n);
        if (n > 0){
            int sum = ((n + 1) * n) / 2;
            printf("%d\n", sum);
        }else{
            break;
        }
    }
}