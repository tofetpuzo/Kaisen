def subtract(a, b):
    return a - b
def add(a, b):
    return a + b - subtract(a, b)
print(subtract(121, 74))
