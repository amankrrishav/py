set1 ={1,24,22,11}
print(set1)

#print(set1[3])

set1.add(32)
print(set1)
set1.remove(32)
print(set1)

set1.discard(100) #wont throw error
print(set1)
#set1.remove(100) #will throw error
#print(set1)

set1.pop() #removes the arbitrary elemtnt
print(set1)

#set1.clear()
#print(set1)

a ={1,2,22,11}
b ={22,3,1}
c= a.union(b)
print(c)

d = a.intersection(b)
print(d)
