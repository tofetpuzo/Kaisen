def discount(num1, num2):
    return (num1 + num2) * 0.1


def total(num1, num2):
    return num2 - num1 - discount(num1, num2)
