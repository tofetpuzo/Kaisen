def subtract(a, b):
    return a - b
def add(a, b):
    return a + b - subtract(a, b)
print(add(121, 74))
