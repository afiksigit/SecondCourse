"""
Made by Afik
"""

# Ex chapter 1

import functools


# 1.1.2
def double_letter(my_str):
    return "".join(map(mirror, my_str))


def mirror(a):
    return a * 2


# 1.1.3
def four_dividers(number):
    return list(filter(is_divided_by_four, range(1, number + 1)))


def is_divided_by_four(number):
    return number % 4 == 0


# 1.1.4
def sum_of_digits(number):
    return functools.reduce(add, str(number))


def add(digit1, digit2):
    return int(digit1) + int(digit2)


# 1.3.1
def intersection(list_1, list_2):
    return [x for x in set(list_1) if x in list_2]


# 1.3.2
def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, number))


# 1.3.3
def is_funny(string):
    return all(char == 'a' or char == 'h' for char in string)


# 1.3.4
# optional task
def recover_password(password):
    return "".join(
        list(map(lambda tav: (chr((ord(tav) + 2 - ord("a")) % 26 + ord("a")) if tav.isalpha() else tav), password)))


# coin challenge
def combine_coins(coin, numbers): return ', '.join(map(lambda s, n: s + str(n), [coin for i in numbers], numbers))


# summarize tasks
def longest_name():
    with open("names") as file:
        return max(file.read().split(), key=len)


def names_length():
    with open("names") as file:
        return functools.reduce(lambda a, b: a + len(b), file.read().split(), 0)


def shortest_names():
    with open("names") as file:
        names = file.read().split()
        min_len = len(min(names, key=len))
        return "\n".join([name for name in names if len(name) == min_len])


def names_length_into_file():
    with open("names") as file, open("name_length.txt", "w") as output_file:
        output_file.write("".join([str(len(name)) + "\n" for name in file.read().split()]))


def name_with_spec_len():
    name_len = int(input("enter name length"))
    with open("names") as file:
        return "\n".join([name for name in file.read().split() if len(name) == name_len])


def main():
    # 1.1.2
    print((double_letter('afik')))

    # 1.1.3
    print(four_dividers(9))

    # 1.1.4
    print(sum_of_digits(154))

    # 1.3.1
    print(intersection([1, 2, 3, 4], [4, 4, 2]))

    # 1.3.2
    print(is_prime(43))

    # 1.3.3
    print(is_funny('haaaaaaha'))

    # 1.3.4
    # optional task
    print(recover_password("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))

    # summarize tasks
    print(longest_name())

    print(names_length())

    print(shortest_names())

    names_length_into_file()

    print(name_with_spec_len())


if __name__ == '__main__':
    main()
