# input()   int()    float()  eval()
#type casting ----------------------(python take any input as string)
#you can cast type for every data type in python

a=input("enter a value:-")                      #text on the quatation is label
b=input("enter another value:-")
print(a+b)                 # will not add rather concatenate because python take input as string

# int type casting
x=int(input("ente int value1:-"))
y=int(input("ente int value2:-"))
print(x+y,"addition of the number you enter")
print(type(x+y))



#flaot type casting
m=float(input("enter a float number"))
n=float(input("enter another float number"))
print(m*n)
print(type(m*n))


#float and int type casting togather but the ans will be in float form
m1=float(input("enter a float number"))
n1=int(input("enter int number"))
print(m1*n1)
print(type(m1*n1))



#eval type casting   eval can take any type of input int,string, float an so on ..........



mx=eval(input("enter anythingr"))
nx=eval(input("enter anything"))
print(mx*nx)
print(type(mx*nx))
