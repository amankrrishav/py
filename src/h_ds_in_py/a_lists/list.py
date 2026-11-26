marks = [80, 90, 100]
print(marks)

multi_dtypes_list = [1, "hello", 45.67, True]
print(multi_dtypes_list)

#list methods

#append() - add to last index
print(marks)
marks.append(100) #adding to last index in org list
print(marks)


#pop() - remove from end
print(marks)
marks.pop() #removing from last index in org list
print(marks)
marks.pop(1)
print(marks)


#extend() - add multiple elements to the end of the list
marks.extend([100, 50, 75]) #this new list will be added to org list marks
print(marks)


#insert() - add element at specific index
marks.insert(1, 85)
print(marks)


#remove() - remove specific value
marks.remove(85)
print(marks)

#clear() - remove all elements
marks.clear()
print(marks)

#del() - remove element at specific index
del marks[1]
print(marks)

#sorted() - sort list in ascending order
marks.sort()
print(marks)

#sorted() - sort list in descending order
marks.sort(reverse=True)
print(marks)

#len() - get length of list
print(len(marks))

#min() - get minimum value of list
print(min(marks))

#max() - get maximum value of list
print(max(marks))

#sum() - get sum of list
print(sum(marks))

#index() - get index of specific value
print(marks.index(85))

#count() - count number of specific value
print(marks.count(85))

#copy() - copy list
marks.copy()
print(marks)

#reverse() - reverse list
marks.reverse()
print(marks)

#sort() - sort list in ascending order
marks.sort()
print(marks)

#sort() - sort list in descending order
marks.sort(reverse=True)
print(marks)

#count() - count number of specific value
print(marks.count(85))
