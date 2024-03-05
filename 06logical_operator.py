#3 logical operator
# "and" returns true if both statemante are true
#"or"  returns true if any of one statemante is true
#"not" rverse the result  if the result is true it will return fals or if the result is flase it will return true

a=30
# there are 3 logical operator "and"   "or"  "not"
b=70
c=78
print("and locical operator")
print(a<b and b>a)
print(a<=30 and c>=555) 
print(a!=20 and b==70)

print("or locikal operator")
print(a>b or b<c)
print(a>=300 or c<=a)
print(a==30 or b==70)

print("not logical operator ")
print(not a!=30)