# None <--- refers here absence of value

dictionaries={
    'name':'sai',
    'age':20,
    'skill':[1,2,3]
}
print(dictionaries)
print(dictionaries['age']) #it returns age value(20)

# get() method
print(dictionaries.get('age'))

# The above two print methods prints same what make differnce using get?
# get method is used ignore error for example
print(dictionaries.get('games')) #it returns None
# print(dictionaries['game']) #it returns error

# if we want to get all the keys in dictionaries
print(dictionaries.keys()) 
print(dictionaries.values()) #returns all the values

dictionaries['gender']='Male' #add gender and value male to dict
print(dictionaries) 

#dictionaries.clear() #clear all
print(dictionaries) 

# copy() method
dictionaries2=dictionaries.copy()
print(dictionaries)
print(dictionaries2)

dictionaries2.popitem() #randomly pop item
print(dictionaries)
print(dictionaries2)

#update() method
dictionaries.update({'lang':'python'})
print(dictionaries)

