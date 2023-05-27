"""
Made by Afik
"""


def check_id_valid(id_number):
    return sum(int(digit) if i % 2 == 0 else sum(int(x) for x in str(int(digit) * 2)) for i, digit in
               enumerate(str(id_number))) % 10 == 0


class IDIterator:
    def __init__(self, id_):
        # Constructor for the IDIterator class.
        # Initializes the ID number attribute.
        #
        # Parameters:
        #   id_ (int): The ID number to start the iterator from.
        #
        self.id_ = id_

    def __iter__(self):
        # Returns the iterator instance itself.
        #
        # Returns:
        #   IDIterator: The iterator instance.
        #
        return self

    def __next__(self):
        # Generates the next valid ID number in the range.
        # Raises StopIteration when the end of the range is reached.
        #
        # Returns:
        #   int: The next valid ID number.
        #
        while self.id_ <= 999999999:
            current_id = self.id_
            self.id_ += 1
            if check_id_valid(current_id):
                return current_id
        raise StopIteration


def id_generator(id_number):
    # Generator function that generates the next valid ID number in the range.
    #
    # Parameters:
    #   id_number (int): The ID number to start the generator from.
    #
    # Yields:
    #   int: The next valid ID number.
    #
    while id_number <= 999999999:
        id_number += 1
        if check_id_valid(id_number):
            yield id_number


def main():
    # The main program that receives user input and generates valid ID numbers.
    id_number = int(input("Enter ID: "))

    iterator_type = input("Generator or Iterator? (gen/it)? ")

    if iterator_type == "it":
        # Use an iterator to generate valid ID numbers.
        id_iter = IDIterator(id_number)
        next(id_iter)  # Skip the first ID number received

        for _ in range(10):
            new_id = next(id_iter)
            print(new_id)
    elif iterator_type == "gen":
        # Use a generator function to generate valid ID numbers.
        id_gen = id_generator(id_number)
        next(id_gen)  # Skip the first ID number received

        for _ in range(10):
            new_id = next(id_gen)
            print(new_id)
    else:
        print("Invalid input. Please enter either 'gen' or 'it'.")


if __name__ == '__main__':
    main()
