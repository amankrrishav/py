# make a dict with 3 student names as keys and marks as values, then print each name and mark in a loop. Hint: look up .items().

names = {"aman":100, "kumar":99,"rishav":72}

for name,marks in names.items():
    print(f"{name} : {marks}")    