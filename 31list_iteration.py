#using range 
# must have a length
l=[11,22,33,44,55,66]
t=len(l)
for a in range(t):  #length 6 loop ta suru hobe 0 theke till 6 ba 5 porjono number generate korbe
    print(l[a])


print()
#list iteration without using range

z=[34,35,3,6,34]
for a in z:
    print(a)

print("")

#reverse a list  
x=[10,20,30,40,50]
t=len(x)   #5
print(t,"amra ulta koira list ta iterate korbo")
for a in range(t-1,-1,-1):
    print(x[a])
    #print(id(x[a]))


print()
#question  ...ekta code likah ..jeta user theke ekta list input nibe ebong seta ulta kore 1 ta ekta kore pint kore dibe

l=eval(input("ekta list input daw"))
t=len(l)
for a in range(t-1,-1,-1):
    print(l[a])