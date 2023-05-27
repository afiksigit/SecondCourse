"""
Made by Afik
"""


class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self.hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self.hunger > 0

    def feed(self):
        self.hunger -= 1

    def talk(self):
        pass

    def special_method(self):
        pass


class Dog(Animal):
    # prints subclass type
    def __str__(self):
        return "Dog"

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!	")

    # activate the special method
    def special_method(self):
        self.fetch_stick()


class Cat(Animal):
    # prints subclass type
    def __str__(self):
        return "Cat"

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")

    # activate the special method
    def special_method(self):
        self.chase_laser()


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    # prints subclass type
    def __str__(self):
        return "Skunk"

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")

    # activate the special method
    def special_method(self):
        self.stink()


class Unicorn(Animal):
    # prints subclass type
    def __str__(self):
        return "Unicorn"

    def talk(self):
        print("Good day. darling")

    def sing(self):
        print("I’m not your toy...	")

    # activate the special method
    def special_method(self):
        self.sing()


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    # prints subclass type
    def __str__(self):
        return "Dragon"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

    # activate the special method
    def special_method(self):
        self.breath_fire()


def main():
    dog = Dog("Brownie", 10)
    dog2 = Dog("Doggo", 80)
    cat = Cat("Zelda", 3)
    cat2 = Cat("Kitty", 80)
    skunk = Skunk("Stinky", 0)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn = Unicorn("Keith", 7)
    unicorn2 = Unicorn("Clair", 80)
    dragon = Dragon("Lizzy", 1450)
    dragon2 = Dragon("McFly", 80)
    zoo_lst = [dog, dog2, cat, cat2, skunk, skunk2, unicorn, unicorn2, dragon, dragon2]

    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal, animal.get_name())  # info about hungry animals
        while animal.is_hungry():
            animal.feed()  # feed hungry animals
        animal.talk()  # animal talk
        animal.special_method()  # animal special method
        print("\n")
    print("Zoo name:", Animal.zoo_name)


if __name__ == '__main__':
    main()
