#chr() will take integer and return its character (ascii)
#ord() will take single character return its ascii number

a=67
print(chr(a))

b="r"
print(ord(b))


x=eval(input("enter an integer digit to see its ascii:-"))
print(chr(x))

y=eval(input("enter any thing without digit to see its ascii:-"))
print(ord(y))