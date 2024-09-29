# beginning with the first step

num1 = 10
num2 = 20

# things
# cart -
# [shoes: 2, price: $4 x 2 = total] , [shirts:  $3 x 2 , pants : $1 price: $1 x 1]
name = "taiwo"
num_shoes = 4
num_shirts = 3
num_pants = 1

name_of_variable = []
quantity_shoes = ""
quantity_shirts = 2
quantity_pants = 1

# list of items, array of items
items = []

items = list()

itemss = dict()
item1 = {"smart": "phone"}
# ["taiwo", num_shoes, num_shirts, num_shirts, quantity_shoes, quantity_shirts, quantity_pants]
# [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]

items_people_bought = [
    "taiwo",
    num_shoes,
    num_shirts,
    num_pants,
    quantity_shoes,
    quantity_shirts,
    quantity_pants,
    "ore",
    num_shoes,
    num_shirts,
    num_pants,
    quantity_shoes,
    quantity_shirts,
    quantity_pants,
    "raliat",
    num_shoes,
    num_shirts,
    num_pants,
    quantity_shoes,
    quantity_shirts,
    quantity_pants,
    "atinuke",
    num_shoes,
    num_shirts,
    num_pants,
    quantity_shoes,
    quantity_shirts,
    quantity_pants,
    "ray231",
    num_shoes,
    num_shirts,
    num_pants,
    quantity_shoes,
    quantity_shirts,
    quantity_pants,
    "adeola",
    num_shoes,
    num_shirts,
    num_pants,
    quantity_shoes,
    quantity_shirts,
    quantity_pants,
    "kayode",
    num_shoes,
    num_shirts,
    num_pants,
    quantity_shoes,
    quantity_shirts,
    quantity_pants,
]
# for
# key -> value
items_people_bought_dict = {
    "teekay": {"price": 1, "quantity": 1, "item": {"shoes", "shirts"}},
    "raymond": {"price": 2, "quantity": 2, "item": "shirts"},
}
# "teekay": {"price": 1, "quantity": 1, "item": {"shoes", "shirts"}} A
# {"price": 1, "quantity": 1, "item": {"shoes", "shirts"} B
# "quantity": 1, "item": {"shoes", "shirts"} C
# print(items_people_bought_dict["teekay"]["price"])
# print(items_people_bought_dict)
# "shirts" A
# item: {"shoes", "shirts"}
# "teekay": {"price": 1, "quantity": 1, "item": {"shoes", "shirts"}},


# print(items_people_bought[7])

# item = [items_people_bought_dict]
# print(type(items_people_bought_dict))
# print(type(item))
# print(item)

# items1 = {1: [], "price": 0, "quantity": bool, 2: "shoes"}


# # data structures and algorithms


# print("num1 + num2 =", num2 - num1)

# 1. strings, int, float, boolean, list, dictionary, tuple, set
# num1 + num2 = 30

# operators are used to perform operations on variables and values
# addition operator
# subtraction operator
# multiplication operator
# division operator
# modulus operator - returns the remainder of a division 13 % 5 = 3

# find ore in the list of items
# for everybody in items_people_bought:
#     print(everybody)


no_of_boys = 12
no_of_girls = 8
no_present = 15


def sum_of_pupils_in_class():
    total_pupils = no_of_boys + no_of_girls
    return total_pupils


def sum_of_pupils_absents():
    total_absents = sum_of_pupils_in_class() - no_present
    return total_absents


sum_of_pupils_in_class()
print(sum_of_pupils_absents())
