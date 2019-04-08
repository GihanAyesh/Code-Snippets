a=input()
for i in range (a):
    hor=input()
    lydia=raw_input()
    ans=""
    for j in range(len(lydia)):
        if lydia[j]=="S":
            ans+="E"
        elif lydia[j]=="E":
            ans+="S"
    print "Case #"+str(i+1)+": "+ans
