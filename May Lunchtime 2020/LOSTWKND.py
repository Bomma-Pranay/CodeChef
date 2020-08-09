# Problem Link : https://www.codechef.com/LTIME84B/problems/LOSTWKND

# My Solution : 

tc=int(input())
for xyz in range(tc):
    l=list(map(int,input().split()))
    p=l.pop()
    for i in range(len(l)):
        l[i]=l[i]*p
    if sum(l)<=120:
        print('No')
    else:
        print('Yes')
