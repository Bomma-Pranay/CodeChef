# Problem Link : https://www.codechef.com/LTIME86B/problems/CHEFSTEP

# My Solution

# Problem 1
tc=int(input())
for xyz in range(tc):
    l=list(map(int,input().split()))
    n,k=l[0],l[1]
    k=k%(1000000001)
    # s=''
    li=list(map(int,input().split()))
    # print(li)
    # print(s)
    s=''
    for i in li:
        if (i%1000000001)%(k)==0:
            s=s+'1'
        else:
            s=s+'0'
    print(s)
