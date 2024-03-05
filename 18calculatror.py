#simple python calculator to perform arithmatic operation

print(""" 
        + for additon
        - for substraction
        * for multiplication
        / for division
        // for floor division
        "%"  for modulas operation
        **  for power 
     """)

a=eval(input("enter your 1st number:-"))
b=eval(input("enter your second number:-"))
opr=input("enter a operator")


if opr== "+":
    print("jogfol ",a+b)
elif opr== "-":
    print("biyogfol ",a-b)
elif opr== "*":
    print("gumfol ",a*b)
elif opr== "/":
    print("vagfol ",a/b)
elif opr== "//":
    print("floor division ",a//b)
elif opr== "%":
    print("vagses ",a%b)
else:
    print("invalid operator")
