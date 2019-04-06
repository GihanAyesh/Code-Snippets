def getPrime(n):
    numPrime=0
    primeArray=[0]
    for i in range (2,n+1):
        sts=True
        for m in range (n):
            if ((primeArray[m] == 0) or (primeArray[m])>int(math.sqrt(i))):
                break
            elif(i%primeArray[m]==0):
                sts=False
                break
        if (sts):
            if primeArray[0]==0:
                primeArray[0]=i
            else:
                primeArray+=[i]
        numPrime+=1
    return primeArray
