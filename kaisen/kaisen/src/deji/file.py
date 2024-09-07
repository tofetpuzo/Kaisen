print ("hello world, my name is Adedeji Awolesi")

#Create a function
def add(a,b):
    add = a + b
    return add
print(add(2,3))

#Write a function that calls another function
def subtract(a,b):
    difference = add(a,b)
    diff = difference - b
    return diff
print(subtract(3,2))


#Write a list of python store that store all things you wants, preferabley names
list = [1,2,3,4,5,6,7,8,9,10]

print(len(list))