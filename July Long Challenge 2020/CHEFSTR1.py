# Problem Link : https://www.codechef.com/JULY20B/problems/CHEFSTR1

# My Solution

tc=int(input())
for xyz in range(tc):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(n-1):
        s=s+abs(l[i+1]-l[i])-1
    print(s)


