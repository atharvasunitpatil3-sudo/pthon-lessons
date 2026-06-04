a = [1,2,3,4]
b = [1,2,3,4]

print(a == b)

# Is identity operator
print(a is b)

#Pthon orogram to illustrate the use 
# of 'is' identity operator

x = 5

if (type(x) is int):
    print("true")
else:
    print("false")

x = 5.5
if (type(x) is not float):
    print("true")
else:
    print("false")

x = 20
y = 20
if (x is y):
    print("x & y SAME identity")