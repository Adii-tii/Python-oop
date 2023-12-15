#without parameters
"""def xyz():
THIS IS XYZ FUNCTION
    print("xyz")
print(xyz.__doc__)
xyz()
def xyz():
    a=4
    print(a)
xyz()

#with parameters
def xyz(a,b):
    print(a,b)
    print (id(a))
a=3
b=4
xyz(a,b)
print (id(a))
"""

#with parameters
"""
def xyz():
    a=3
    b=4
    return a+b
print(xyz())
"""

#finding even and odd numbers 
def even(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
n=int(input("enter the number here: "))
print(even(n))