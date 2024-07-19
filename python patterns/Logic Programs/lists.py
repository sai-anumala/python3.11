# to add elements
# append it adds an element at the end of your list
# insert insert(3,'a')

# remove methods
# pop() or pop(2) <---that index
# remove(x) <---by value
# clear() <---- deletes all

#look up methods
# index(x) <---returns the index value of x
# in checks the wether element exists or not return on boolen value(true or not)
# sort()


list=[1,2,3,4,5]
list2=['a','b','c']
list3=[1,2,'a',True]

#assigning list address to another list 
amazon_cart=['notebooks','sunglasses']
new_cart=amazon_cart
new_cart[0]='pencils' #if a change occurs in new list which is having other list will effect it
#print(amazon_cart,new_cart)

#if we want to not change in original list we should do add [:]at end of assining address of original list
amazon_cart2=['notebooks','sunglasses']
new_cart2=amazon_cart2[:]
new_cart2[0]='books'
#print(amazon_cart2,new_cart2)

#2-Dimensional array
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#print(matrix[1][1]) #it will print 2 list's (index having 1) 2nd element(index having 1)

#adding elements to list (append)
#by using append method we can add only one element 
#append method takes only one argument
list=[1,2,3,4,5]
list.append(6) #adding 6 at end of the list
#print(list)

#adding elements at desired index  (insert method)
list.insert(0,0)
#print(list)

#pop method (removes by index)
list.pop() #it removes last element
list.pop(0) #it removes 0th index element

#remove method (removes by value)
list.remove(4) #it removes the 4(value) from the list
#print(list)

#extend method
#we can add multiple elements to list by using extend (upgrade version of append)
list.extend([6,7])
#print(list)

#clear
list.clear() #it removes all the elements in the list
#print(list)

#look up ,methods(index,in)
#index
test=[1,2,3,4,5]
#print(test.index(2,0,2)) #checking value 2 on btwn index 0 to 2

#in 
print(3 in test)

#count method
test=[1,2,33,3,4,4]
print(test.count(4)) #it returns the number of 4 in list/array

#sort method
test.sort() #we cannot write it directly in print method
print(test)

#copy method
test2=test.copy() #copies the test list/array
print(test2)

#reverse method
test2.reverse()
print(test2)
print(test2[::-1]) #another method for reverse

# List using range() keyword
#print(list(range(1,10))) #it returns the 1 to 9 elements

#join method
newSentence=' '.join(['hi','my','name','is','sai'])
print(newSentence)

# List unpacking
a,b,c = [1,2,3] #it will assigns the each list element to each variable
print(a,b,c)
print(a) #it returns the one value which is 1

# other unpacking method
e, *other=[5,6,7] # here *other is pointeer for other elements
print(e,other) #it returns remaining list op:5,[6,7]