"""
Made by Afik
"""


class Lion:
    count_animals = 0

    def __init__(self, age, name="mufasa"):
        self._age = age
        self._name = name
        Lion.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        color = ""
        if self._red == 0 and self._green == 0 and self._blue > 50:
            color = "Blue"
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            color = "Green"
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            color = "Red"
        print(f"X:{self._x},Y:{self._y}, Color: ({self._red},{self._green},{self._blue}) {color}")


# ex 2.4.2
class BigThing:
    def __init__(self, something):
        self.something = something

    def size(self):
        if isinstance(self.something, (int, float)):
            return self.something
        elif isinstance(self.something, (list, dict, str)):
            return len(self.something)
        else:
            return None


class BigCat(BigThing):
    def __init__(self, something, weight):
        super().__init__(something)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Vert Fat"
        elif self.weight > 15:
            return "Fat"
        else:
            return "Ok"


def main():
    # 2.2 + 2.3.3
    lion1 = Lion(10)
    lion2 = Lion(5, "Tim")
    lion1.birthday()
    print("age:", lion1.get_age())
    print("age:", lion2.get_age())

    print("Name:", lion1.get_name())
    print("Name:", lion2.get_name())
    lion1.set_name("yossi")
    print("New Name:", lion1.get_name())
    print("Animals amount:", Lion.count_animals)

    # 2.3.4
    pixel = Pixel(5, 6, 250)
    pixel.print_pixel_info()
    pixel.set_grayscale()
    pixel.print_pixel_info()

    # ex 2.4.2
    # Create an instance of BigThing with a number
    big_num = BigThing(42)
    print(big_num.size())  # Output: 42
    # Create an instance of BigThing with a list
    big_list = BigThing([1, 2, 3, 4, 5])
    print(big_list.size())  # Output: 5
    # Create an instance of BigThing with a string
    big_str = BigThing("Hello, world!")
    print(big_str.size())  # Output: 13
    # Create an instance of BigCat with a string
    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
