l=[12,34,56,67]
print(l[2],"3rd element ")  #get the data from l in index 2
print(l[0],"first element")
print(l[1],"second element")
print(l[3],"4th elament")
print(len(l),' is the lenght of l')


#how to work with nested list
m=[[1,2,3,4],[11,22,33,44]] #this is a nested list
print(m)
print(len(m))
print(m[1][1])  # list er 1 number index er list theke 1num undex er data daw
print(m[0][3])  #list er 0 number index ee j list ache tar 3 num index er data daw
print(m[0])
print(m[1])


#list slicing 
x=[11,22,33,44,55,66]
print(x[0:2])               #[0:2] er moddhe o hocche starting index   2 hocche increment <2 ba 0 theke suru kore <2 


m=[100,200,300,400,500]
print(m[1:4])





#get the data 1 3 5 7 from the list
l=[1,2,3,4,5,6,7]
print(l[0::2])  # 0 hocche start form index 0 ,2 is the ittaration ---(ba 1ta nibe 1ta phaka rakhe r ekta nibe emon kore )


#how to get list from reverse or reverse the list
l=[12,13,14,15,16]
print(l[-1::-1])
