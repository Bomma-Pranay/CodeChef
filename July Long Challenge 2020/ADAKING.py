# Problem Link : https://www.codechef.com/JULY20B/problems/ADAKING

# My Solution 

tc=int(input())
for xyz in range(tc):
    k=int(input())
    # k=12
    l0=['X']*8
    l1=['X']*8
    l2=['X']*8
    l3=['X']*8
    l4=['X']*8
    l5=['X']*8
    l6=['X']*8
    l7=['X']*8
    l0[0]='O'
    if k<=8:
        for i in range(1,k):
             l0[i]='.'
        [print(i,end='') for i in l0]
        print()
        [print(i,end='') for i in l1]
        print()
        [print(i,end='') for i in l2]
        print()
        [print(i,end='') for i in l3]
        print()
        [print(i,end='') for i in l4]
        print()
        [print(i,end='') for i in l5]
        print()
        [print(i,end='') for i in l6]
        print()
        [print(i,end='') for i in l7]
        print()
    else:
        rows=k
        k=k-1
        k=k%8
        if 9<=rows<=16:
            #change l1
            # [lo[j]='.' for j in range(8)]
            for j in range(1,8):
                l0[j]='.'
            for i in range(k+1):
                l1[i] = '.'
            [print(i, end='') for i in l0]
            print()
            [print(i, end='') for i in l1]
            print()
            [print(i, end='') for i in l2]
            print()
            [print(i, end='') for i in l3]
            print()
            [print(i, end='') for i in l4]
            print()
            [print(i, end='') for i in l5]
            print()
            [print(i, end='') for i in l6]
            print()
            [print(i, end='') for i in l7]
            print()

        elif 17 <= rows <= 24:
            # change l2
            for j in range(1, 8):
                l0[j] = '.'
            for j in range(8):
                l1[j] = '.'
            for i in range(k+1):
                l2[i] = '.'
            [print(i, end='') for i in l0]
            print()
            [print(i, end='') for i in l1]
            print()
            [print(i, end='') for i in l2]
            print()
            [print(i, end='') for i in l3]
            print()
            [print(i, end='') for i in l4]
            print()
            [print(i, end='') for i in l5]
            print()
            [print(i, end='') for i in l6]
            print()
            [print(i, end='') for i in l7]
            print()

        elif 25 <= rows <= 32:
            # change l3
            for j in range(1, 8):
                l0[j] = '.'
            for j in range(8):
                l1[j] = '.'
            for j in range(8):
                l2[j] = '.'
            for i in range(k+1):
                l3[i] = '.'
            [print(i, end='') for i in l0]
            print()
            [print(i, end='') for i in l1]
            print()
            [print(i, end='') for i in l2]
            print()
            [print(i, end='') for i in l3]
            print()
            [print(i, end='') for i in l4]
            print()
            [print(i, end='') for i in l5]
            print()
            [print(i, end='') for i in l6]
            print()
            [print(i, end='') for i in l7]
            print()

        elif 33 <= rows <= 40:
            # change l4
            for j in range(1, 8):
                l0[j] = '.'
            for j in range(8):
                l1[j] = '.'
            for j in range(8):
                l2[j] = '.'
            for j in range(8):
                l3[j] = '.'
            for i in range(k+1):
                l4[i] = '.'
            [print(i, end='') for i in l0]
            print()
            [print(i, end='') for i in l1]
            print()
            [print(i, end='') for i in l2]
            print()
            [print(i, end='') for i in l3]
            print()
            [print(i, end='') for i in l4]
            print()
            [print(i, end='') for i in l5]
            print()
            [print(i, end='') for i in l6]
            print()
            [print(i, end='') for i in l7]
            print()

        elif 41 <= rows <= 48:
            # change l5
            for j in range(1, 8):
                l0[j] = '.'
            for j in range(8):
                l1[j] = '.'
            for j in range(8):
                l2[j] = '.'
            for j in range(8):
                l3[j] = '.'
            for j in range(8):
                l4[j] = '.'
            for i in range(k+1):
                l5[i] = '.'
            [print(i, end='') for i in l0]
            print()
            [print(i, end='') for i in l1]
            print()
            [print(i, end='') for i in l2]
            print()
            [print(i, end='') for i in l3]
            print()
            [print(i, end='') for i in l4]
            print()
            [print(i, end='') for i in l5]
            print()
            [print(i, end='') for i in l6]
            print()
            [print(i, end='') for i in l7]
            print()

        elif 49 <= rows <= 56:
            # change l6
            for j in range(1, 8):
                l0[j] = '.'
            for j in range(8):
                l1[j] = '.'
            for j in range(8):
                l2[j] = '.'
            for j in range(8):
                l3[j] = '.'
            for j in range(8):
                l4[j] = '.'
            for j in range(8):
                l5[j] = '.'
            for i in range(k+1):
                l6[i] = '.'
            [print(i, end='') for i in l0]
            print()
            [print(i, end='') for i in l1]
            print()
            [print(i, end='') for i in l2]
            print()
            [print(i, end='') for i in l3]
            print()
            [print(i, end='') for i in l4]
            print()
            [print(i, end='') for i in l5]
            print()
            [print(i, end='') for i in l6]
            print()
            [print(i, end='') for i in l7]
            print()

        elif 57 <= rows <= 64:
            # change l7
            for j in range(1, 8):
                l0[j] = '.'
            for j in range(8):
                l1[j] = '.'
            for j in range(8):
                l2[j] = '.'
            for j in range(8):
                l3[j] = '.'
            for j in range(8):
                l4[j] = '.'
            for j in range(8):
                l5[j] = '.'
            for j in range(8):
                l6[j] = '.'
            for i in range(k+1):
                l7[i] = '.'
            [print(i, end='') for i in l0]
            print()
            [print(i, end='') for i in l1]
            print()
            [print(i, end='') for i in l2]
            print()
            [print(i, end='') for i in l3]
            print()
            [print(i, end='') for i in l4]
            print()
            [print(i, end='') for i in l5]
            print()
            [print(i, end='') for i in l6]
            print()
            [print(i, end='') for i in l7]
            print()

