a =5
table=[]
for i in range(1,11): #ran a loop from 1 to 10
    table.append(a*i) #a will remain constant and the i in each iteration will get multiplied by a  
print(table) #produces list of 5's table

#now list comprehension will do the sam e thing in a single line 

table1 = [a*i for i in range(1,11)] #syntax =
print(table1)