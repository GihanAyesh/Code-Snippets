def primeList(n):
    lis=[]
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n): 
        if prime[p]: 
            lis+=[p]
    return lis
 

alp=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
t = input()
for a in range (t):
    sts=map(int, raw_input().strip().split())
    n,l=sts[0],sts[1]
    data = map(int, raw_input().strip().split())
    primes = primeList(n)
    order = []
    for q in range(l-1):
        if data[q]==data[q+1]:
            continue
        else:
            for j in primes:
                if (data[q]%j==0) and (data[q+1]%j==0):
                    order.append(data[q]/j)
                    order = [data[q]/j,j]*(q/2)+order
                    if q%2!=0:
                        order = [j]+order
                        break
            break
    for k in range (q,l):
        order.append(data[k]/order[-1])
    q = set(order)
    q=sorted(q)
    output = ''
    for i in order:
        output+=alp[q.index(i)]
    print 'Case #'+str(a+1)+':',output
