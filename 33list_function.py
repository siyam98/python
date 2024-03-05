# del()
# pop()
# remove()
# clear()

#del function  
l1=[11,22,33,44,55] # tumi 2 number index er element ta delete kore daw mane 33 ta list theke delete kore daw 
del l1[2]           # del likhe list er nam ebong tar j index er ta gayeb korte caw opita pass korte hobe
print(l1)



l2=['siyam','moon','tor',11.23]
del l2[0]    #del function er sathe print use kora jai nah 
print(l2)



#pop() use to remove element also work with index
m=[22,33,44,55]
print('3number index er element 55 pop koira dichi',m.pop(3))
print(m)


#remove() function in list

num=[100,80,75,70,60,50]
num.remove(50)   # u will pass the elemant you want to remove 
print(num)


num=[100,80,75,70,50,50]
num.remove(50)   # u will pass the elemant you want to remove 
print(num)


#clear() function in list
c=[12,32423,5546,7,5867,9,78978]
c.clear()
print(c,"dekcho blak list return diche ")


#update element to a list

li=[23,45,546,7785]
li[0]=10000002
li[2]=69696969
print(li)


print("///////////////////////////////////////////////////////////////////////////")
# insert()
# append()
# extends()
m1=[11,22,33,44,55,66]
m1.insert(0,100) #1st ee index number ,,2nd ee value 
print(m1)
print(len(m1))

print()


m2=['siya','shahriar','moon','shourov']
m2.insert(0,'md')  #index kotote oitar number ,,,,oi index er element
print(m2)


#append   eita sobar las ee elemrt jog korbe
n1=[1,2,3,4]
n1.append(5)    #only pass the element
print(n1)

# nested list uning append

n4=[1,2,3,4,5]
n5=['moon','sun']
n4.append(n5)
print(n4)


# extends()  elemtnt add korbe to the existing lis
k=[99,98,97,96]
k1=[95,94]
k.extend(k1)
print(k)