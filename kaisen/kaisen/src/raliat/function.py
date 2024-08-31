def subtract(a, b):
    return a - b

def add(a, b):
    difference = subtract(a, b)
    return a + b, difference

result, difference = add(10, 5)
print(f"Addition result: {result}")
print(f"Subtraction result: {difference}")