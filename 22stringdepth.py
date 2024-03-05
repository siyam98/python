# string  indexing and sliceing
#string can be created by enclosing characters inside single/double quotes
# triple quote used to creat multiline string
#each character of string has it index 
#example  "siyam"   (s in index 0 )  (i in index 1) (y in index 2) (a in index 3 ) (m in index 4)
#index always start from 0 and continue in sequence(for left to right)
#if you count index from right side it will start from index (-1) and continute like -1,-2.-3,-4...n 
#any space in a string will aslo count as a charcter of that string, and will have a index too
# index number = total number of character - 1 (since its start with zero)
#string is immutable



#how to get a charcter from a string using index number (from left to right index)
nam="md siyam"
print(nam[2],"ei index a ekta space ache tai phaka")
print(nam[1])
print(nam[7])

print()
#get a character from a string using negative index number(from right to left)
a="mango"
print(a[-1],"o is in -1 index")
print(a[4],"o is in index 4")

print()

print(a[-3],"n is in -3 index")
print(a[2],"a is in index 2")

print()

print(a[-5],"m is in -5 index")
print(a[0],"a is in index 0")

print()
#string slicing: if you want a slice from your string 

name="md siyam shahriar"
print(name[0:8])            #if you want to slice "md siyam portion"
print(name[-15:-12])



#jodi tumi chaw 1ta bade character por por asbe 
x="siyamshahriar"
print(x[0:])  #will print everything from index zero
print(x[0::2])  # 1ta ta charecter bade bade baki gula print korbe

print()
#how to reverse a string
ab="bangladesh"
print(ab[-1::-1])

