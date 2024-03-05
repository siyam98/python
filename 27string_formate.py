nam="hi {} welcome to {}".format("siyam","bangladesh")   
print(nam)

nam1="hi {1} welcome to {0}".format("siyam","bangladesh")   #{} er moddhe idex ta dawa hiche
print(nam1)


nam2="hi {a} how {b} you".format(a="urmi",b=10)            #{} er modde variable er nam gula dawa hoiche
print(nam2)

print()

# write a small proggrm that take some one name and the county he wants to visit and print hi "name" welcome to "country"

#a=eval(input("apnar nam ki"))
#b=eval(input("kon county te jite chan"))
st="hi {a} welcome to {b}".format(a=eval(input("apnar nam ki")),b=eval(input("kon county te jite chan")))
print(st)