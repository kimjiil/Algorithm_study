#별 찍기 11

import sys

input = sys.stdin.readline

N = int(input()) # 3 x 2^k , 3, 6, 12, 24, 48

'''
k = 0 
bb*bb
b*b*b
*****

k = 1

bbbbb*bbbbb
bbbb*b*bbbb
bbb*****bbb
bb*bbbbb*bb
b*b*bbb*b*b
*****b*****

k = 2
                  bbbbb*bbbbb                   
                  bbbb*b*bbbb                   
                  bbb*****bbb                   
                  bb*bbbbb*bb                   
                  b*b*bbb*b*b                   
                  *****b*****                   
                 *bbbbbbbbbbb*                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****   


'''


def draw(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    l = []
    stars = draw(n // 2)
    for star in stars:
        l.append(' ' * (n // 2) + star + ' ' * (n // 2))

    for star in stars:
        l.append(star + ' ' + star)

    return l

l = draw(N)
print('\n'.join(l))