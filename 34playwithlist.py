# Q1...ekta code likho jeta ekta string input nibe, ebon oitak list ee convert korbe , erpor oi lis theke j kono ekta index input nibe 
#ebong oita gayeb kore dibe at the samne time gayew howa elemnt konta oitaw dekhabe 

x=str(input("ekta string inpu daw"))
n=[a for a in x]
print('this is your list',n)
print(n.pop(int(input("index number daw"))))
print(n)



# write a proggram taht take input a list and going to ask you which index eleemnt you want to delet and return it o you
l=eval(input("ekta list input den"))
print(l)
print("list theke kon index er lelmnt delet korte chan oitar index input den")
del l[int(input("index number"))]
print(l)