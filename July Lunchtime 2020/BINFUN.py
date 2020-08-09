# Problem Link : https://www.codechef.com/LTIME86B/problems/BINFUN

# My Solution


def f(a,b):
    # print()
    bx=bin(a).replace("0b","")
    by=bin(b).replace("0b","")
    # print('bx is ',bx)
    # print('by is ',by)
    ibx=bx+by
    iby=by+bx
    # print('ibx is ', ibx)
    # print('iby is ', iby)
    # print('int(ibx, 2) is ', int(ibx, 2))
    # print('int(iby, 2) is ', int(iby, 2))
    return int(ibx,2) - int(iby,2)

tc = int(input())
for xyz in range(tc):
    n=int(input())
    l = list(map(int, input().split()))
    # ans = f(l[0], l[1])
    # ans=0
    if n==1:
        print(0)
    else:
        ans=[]
        for i in range(n):
            for j in range(n):
                d=f(l[i],l[j])
                ans.append(d)
                # print('d is ',d)
                # print('ans is ', ans)
                # ans=max(ans,d)
        print(max(ans))
