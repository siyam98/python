w="moon"   #index 0,1,2,3 
t=len(w)    #length 4 
for a in range(t):   # start hocche o theke jabe <t porjonto , 1 kore increment hobe
    print(w[a])    # 1st loop w[a]=w[0]=m  ; 2nd loop w[a]=w[1]=o ; 3rd loop e w[a]=w[2]=o ; 4th loope w[a]=w[3]=n   



print()
#how to reverse a string index
    
nam=str(input("tomar nam likho:-"))
nam=nam[-1::-1]                        #string slice kore reverse kore dilam eita not proper way
x=len(nam)
for a in range(x):
    print(nam[a])



print()
#proper way to reverse a string with itaration
name1="shahriar"
s=len(name1)
for a in range(s-1,-1,-1):
    print(name1[a])



