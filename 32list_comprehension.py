#list comprehension
#using loop  and append()  function

l=[]
for a in range(1,20,2):
    #print(a)
    l.append(a)
print(l)

nam=[]
for x in range(0,17):
    #print(x)
    nam.append(x)
print(nam)

print("---------------------------------------------------------------------------------------------------------")
#for loop in variable to creat list,,,,,, this know as list comprehension

a=[l for l in range(1,7)]
print(a)

print("-------------------------------------------------------------------------------------------------------")
#list comprehension er vitore add some filter 
# ekta list banaw jeta 1-10 porjonto  sundu matro even number gula list ee rakhbe
l=[h for h in range(1,30) if h%2==0]
print(l)



#how to put /comver a string into a list
x="siyam"
lx=[a1 for a1 in x]
print(lx)