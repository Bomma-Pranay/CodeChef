# Problem Link : https://www.codechef.com/LTIME86B/problems/CHECHOC

# My Solution


tc = int(input())
for xyz in range(tc):
    l = list(map(int, input().split()))
    n, m, x, y = l[0], l[1], l[2], l[3]
    f = 1
    if n % 2 != 0 and m % 2 != 0:
        f = 0
    else:
        f = 1

    d = (n * m) // 2

    if f == 1:
        if (y - x) >= x:
            print(n * m * x)
        else:
            if x<y:
                print(x * d + (y - x) * d)
            elif x>=y:
                print( y* d )

    else:
        if (y - x) >= x:
            print(n*m*x)
        
        else:
            if x<y:
                print(x * d + (y - x) * d +  x)
            elif x>=y:
                print(y * d + y )
