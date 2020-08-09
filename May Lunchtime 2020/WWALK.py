#Problem link : https://www.codechef.com/LTIME84B/problems/WWALK

#My Solution : 

tc = int(input())
for xyz in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ca=[]
    cb=[]
    ca.append(a[0])
    cb.append(b[0])
    for i in range(1,n):
        ca.append(ca[i-1]+a[i])
    for i in range(1,n):
        cb.append(cb[i-1]+b[i])
    #print(ca,cb)
    c = 0
    if ca[0]==cb[0]:
        c=c+ca[0]
    if n==1:
        if ca[0]==cb[0]:
            print(ca[0])
        else:
            print(0)
    else:
        for i in range(n-1):
            if (ca[i]==cb[i]) and (ca[i+1]==cb[i+1]):
                c=c+(ca[i+1]-ca[i])
        #if (ca[-1]==cb[-1]) and (ca[-2]==cb[-2]) :
        #    c=c+(ca[-1]-ca[-2])
        print(c)
