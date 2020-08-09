# Problem Link : https://www.codechef.com/JULY20B/problems/CRDGAME

# My Solution

def pwr(n):
    x=n
    s=0
    while x!=0:
        s=s+x%10
        x=x//10
    return s

tc=int(input())
for xyz in range(tc):
    n=int(input())
    cc=0;cm=0
    for xyzxyz in range(n):
        l=list(map(int,input().split()))
        c,m=l[0],l[1]
        p1,p2=pwr(c),pwr(m)
        if p1>p2:
            cc+=1
        elif p1<p2:
            cm+=1
        else:
            cc+=1
            cm+=1
    if cc>cm:
        print('0',cc)
    elif cc<cm:
        print('1',cm)
    else:
        print('2',cc)


