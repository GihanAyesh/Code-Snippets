a=input()
for i in range (a):
    b=input()
    c=list(str(b))
    ans1,ans2="",""
    if ('4' in c):
        for j in range (len(c)):
            if c[j]=='4':
                ans1+="2"
                ans2+="2"
            else:
                ans1+=c[j]
                if (ans2!=""):
                    ans2+="0"
        print "Case #"+str(i+1)+": "+ans1+" "+ans2
    else:
        print "Case #"+str(i+1)+": "+str(b)
    
               
        
