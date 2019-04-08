from sys import stdin,stdout
import sys

def pattern(n,t):
    ans=""
    while (len(ans)<t):
        ans+="0"*n+"1"*n
    ans=ans[0:t]
    return ans


a=input()
for i in range (a):
    dt=map(int,raw_input().split())
    n,b,f=dt[0],dt[1],dt[2]
    lis,ans=[],[]
    giv=""
    for i in range (f):
        if (2**i>=n):
            break
        print pattern(i+1,n)
        sys.stdout.flush()
        a=raw_input()
        lis+=[a]
    print lis
    for j in range (n-b):
        c=""
        for k in range(len(lis)):
            c+=lis[k][j]
        c=c[::-1]
        g=int(c,2)
        ans+=[g]
    for n in range(n):
        if (n not in ans):
            giv+=str(n)+" "
    print giv
    sys.stdout.flush()
    p=input()
exit()
           
           
