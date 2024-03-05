#dictionany  unordered collection of key-value pais
#each key has to unique
#its a mutable datatype


d={
    'name':'siyam',
    'age':'25',
    'weight':'76kg'
}

print(d,type(d))

#has no index so to get any data we use key
b={'key1':'45','key2':'hi','key3':'tor'}
print(b["key1"])
print(b["key3"])
print(b)


#mutable dat type

m={'key1':'value1','key2':'value2'}
m['key1']='siyam'                    #work on key not index
print(m)



j={
    'tk':'45356654',
    'usd':'97344',
    'aud':'649838'

}
j['tk']='taki tk '
j['aud']='dollar ee dollar'
print(j,type(j))
