a="md siyam shahriar"
print(a.upper())           # sob gula capitral korbe
print(a.lower())           #sob gula small korbe
print(a.title())           #each word er 1st character ta capital korbe
print(a.capitalize())      #just 1st word ta capital korbe


x="welcome"
print(x.find('e'))                           # will start finding from index 0 and will return the index where its desire data will be found first ..even if 
                                             # there is a repeted value always return the one wich its found first ,so in taht case it is in index 1

print(x.find('e',2))                         # find e | and starting from index 2

                                             #if you search any value witch is not present in the string it will return -1

print(x.find('f'))                           #f is not present in welcome


print()
#index function

print(x.index('c'))                           #index 3
# print(x.index("z"))                           #z is not present so it will through error



#find()   if not found will return -1
#index()  if not found will throw error in run-time

print()
m="siyam"
n="2324"
o="232ghg"
print(m.isalpha())  #return true if each char is alphabet
print(n.isdigit())  #return true if each char is digit
print(o.isalnum())  #true true if have both digit & number|| return true for both digit or alphabet 
print(m.isalnum())  #true
print(n.isalnum())  #true

k="siyam123#$"
print(k.isalnum()) #return false since it consist of special character 