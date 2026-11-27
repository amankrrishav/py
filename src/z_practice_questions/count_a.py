# count how many times the letter "a" appears in a string. Write it as a function, count_a(s), and test it on "banana" (expect 3) and "xyz" (expect 0).

def cnt_a(s):
    count = 0
    for char in s:
        if char == 'a':
            count+=1

    return count

print(cnt_a("banana"))        
print(cnt_a("xyz"))

        

