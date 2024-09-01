# Add two numbers

import socket
from datetime import date as Date

import requests


def add(a, b):
    return a + b


# do a multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# take input from user
def take_input():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    return print("number the result of the numbers I added: ", add(a, b))


# age of a person
def age():
    age = int(input("Enter your user: "))
    if age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")
    return age


def calculate_age():
    age = int(input("Enter your age: "))

    current_year = Date.today().year
    birth_year = current_year - age
    print(type(birth_year))
    return print(birth_year)


def get_ip_address_all_users():
    pass


# person from a given ip address
# www.giveawayoftheday.com › ip-address-lookup 345.34.5.5


def ip_info():
    ip_address = input("Enter an IP address : ")
    response = requests.get(f"http://ip-api.com/json/{ip_address}")
    data = response.json()
    print(f"IP: {data['query']}")
    print(f"Country: {data['country']}")
    print(f"City: {data['city']}")
    print(f"Region: {data['regionName']}")
    print(f"ISP: {data['isp']}")
    print(f"ZIP: {data['zip']}")
    print(f"Latitude: {data['lat']}")
    print(f"Longitude: {data['lon']}")
    print(f"Timezone: {data['timezone']}")
    print(f"AS: {data['as']}")


# use request information from api
def get_data():
    import requests

    response = requests.get("https://www.gov.uk/bank-holidays.json")
    return response.json()["england-and-wales"]["events"]


def get_ip_address_from_dns():
    host = "www.google.com"

    return socket.gethostbyname(host)


print(get_ip_address_from_dns())


if __name__ == "__main__":
    # take_input()
    # multiplication_table(51)
    # get_ip_address_all_users()
    # age()
    # calculate_age()
    # print(get_data())
    #
    #
    #
    print(ip_info())
