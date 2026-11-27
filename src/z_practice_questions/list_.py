#Make a list of 5 numbers. Print the largest, the smallest and the sum (use max, min, sum).

list1 = [1,11,12,13,14]
print(list1)
print(max(list1))
print(min(list1))
print(sum(list1))

#given any list print only numbers greater than 10
def num_check(list2):
    for num in list2:
        if num > 10:
            print(num)


print(num_check([1,2,3,4]))
print(num_check([10,11,12,12]))