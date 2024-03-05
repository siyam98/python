#list slicing 

l=[12,30,45,56,'hi']
print(type(l))
print(l[1],l[4]) #30, hi 
print(l[0:3]) #index 0 the ,<3 ba 2 number index porjono

print(l[1::]) #index 1 theke purata  [30,45,56,'hi]

print(l[1:4:2])    #index 1 theke index 4< ba 3 porjo read korbe 2 kore kore increment korbe

print(l[0::1]) #index 0 the purata read korbe 1 1 kore agabe [12,30,45,56,'hi']

print(l[0::2]) #index 0 the purata read korbe 2 2 kore agabe [12,45,'hi']

print()
#reverse slicing 

m=[22,33,44,55,'cat']
print([m[-1]]) #cat
print(m[-1],m[-5]) # cat 22

print(m[-1::-1]) # strat from -1index go till end  and -1 kore agabe

print(m[-2::-2]) #start from index -2  read korbe purata -2 -2 kore agabe [55,33]

print(m[-1:-4:-1]) #['cat',55,44]
