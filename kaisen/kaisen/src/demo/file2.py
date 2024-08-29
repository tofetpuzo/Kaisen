# objected oriented programming
class File2:
    def __init__(self):
        self.name = "File2"
        self.path = "Kaisen/kaisen/kaisen/src/demo/file2.py"
        self.content = "This is file 2"
        self.size = 100
        self.owner = "Kaisen"
        self.group = "Kaisen"
        self.permissions = "rwxr-xr-x"
        self.creation_time = "2021-10-10 10:10:10"
        self.modification_time = "2021-10-10 10:10:10"
        self.access_time = "2021-10-10 10:10:10"

    def get_name(self):
        return self.name

    def get_path(self):
        return self.path

    def get_content(self):
        return self.content

    def get_size(self):
        return self.size

    def get_owner(self):
        return self.owner

    def get_group(self):
        return self.group

    def get_permissions(self):
        return self.permissions

    def get_creation_time(self):
        return self.creation_time

    def get_modification_time(self):
        return self.modification_time

    def get_access_time(self):
        return self.access_time

    def set_name(self, name):
        self.name = name

    def set_path(self, path):
        self.path = path

    def set_content(self, content):
        self.content = content

    def set_size(self, size):
        self.size = size


class Animal:
    def __init__(self):
        self.name = "Animal"
        self.age = 0
        self.color = "Brown"
        self.size = "Medium"
        self.weight = 50
        self.sound = "Roar"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_weight(self):
        return self.weight

    def get_sound(self):
        return self.sound

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Dog"
        self.sound = "Bark"
        self.color = "White"
        self.size = "Small"
        self.weight = 20

    def get_sound(self):
        return self.sound

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_weight(self):
        return self.weight

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Cat"
        self.sound = "Meow"
        self.color = "Black"
        self.size = "Small"
        self.weight = 10

    def get_sound(self):
        return self.sound

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_weight(self):
        return self.weight

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age
