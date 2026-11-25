# in py the string  original 1 cant be changed to smtg else in memory. 
# we can make a new one using org 1 but cant change org 1.

#lets see methods in str

name = "aman" 
print (name)
print (len(name))
print (name.upper())
print (name.lower())
print (name.capitalize(), name)
print (name.title())

print("\n-----------")

text =" hello world "
print(len(text))
print(text.strip())
print(text.lstrip())
print(text.rstrip())

print("\n-----------")

strr = "i am human"
print(strr.find("i"))
print(strr.replace("i","me"))

print("\n-----------")

txt =" pic,game,app "
print(txt.split(","))
print(",".join(['pic','game','beer']))

print("\n-----------")
print(txt.isalpha())
print(txt.isdigit())
print(txt.isalnum())
print(txt.isspace())
