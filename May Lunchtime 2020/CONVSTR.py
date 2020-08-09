#Problem link : https://www.codechef.com/LTIME84B/problems/CONVSTR

#My solution

# cook your dish here
tc=int(input())
for xyz in range(tc):
    n=int(input())
    p=input()
    q=input()
    if p==q:
        print(0)
    else:
        f=1
        for i in range(n):
            if p[i]=='a' and q[i]=='b':
                f=0
                break
        if p.count('b')==n:
            f=0
        if f==0:
            print(-1)
        else:
            idx=[]
            if p.count('a')!=0:
                ind=p.index('a')
            for i in range(n):
                if (p[i]=='b' and q[i]!='b') or (p[i]=='b' and q[i]=='b'):
                    idx.append(i)
            print(1)
            print(len(idx)+1,end=' ')
            #if p.count('a') != 0:
            #print(ind,end=' ')
            idx.append(ind)
            idx.sort()
            for i in range(len(idx)):
                print(idx[i],end=' ')
            print()
        
