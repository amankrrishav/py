tu =(3 , 2 , 1,21)
#tuple unpacking (assigning values of tuple to variables)
a, b, c, d = tu 
print(a)
print(b)
print(c)
print(d) 

# Tuple packing 
tu1 = (
    "meta",
    1,
    43,
    32,32
)

print(tu1)

#unpacking with loops 

for i in tu1:
    print(i)

print(tu1.count(1))    