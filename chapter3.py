"""
Made by Afik
"""


# Exercise 3.1.3
def throw_stop_iteration():
    iterator = iter([])
    next(iterator)


def throw_zero_division():
    x = 5 / 0


def throw_assertion_error():
    assert False, "This is an assertion error"


# method that gives an error
# def throw_import_error():
#     import nonexistent_module

def throw_key_error():
    my_dict = {}
    value = my_dict["nonexistent_key"]


def throw_syntax_error():
    eval("print('Hello, World!'")


# method that gives an error
# def throw_indentation_error():
#     def my_function():
#     print("Indented line")

def throw_type_error():
    x = "Hello"
    y = 5
    z = x + y


# Function to call each function and catch the exceptions
def execute_functions():
    functions = [
        throw_stop_iteration,
        throw_zero_division,
        throw_assertion_error,
        # throw_import_error,
        throw_key_error,
        throw_syntax_error,
        # throw_indentation_error,
        throw_type_error
    ]

    for func in functions:
        try:
            func()
        except Exception as e:
            print(f"Exception caught: {type(e).__name__}")
        else:
            print("No exception was raised")


# Exercise 3.2.5
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return f"__CONTENT_START__\n{content}__CONTENT_END__"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"


# Exercise 3.3.2
class UnderAge(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return f"Your age is {self._age},it is less than 18.In {18 - self._age} years, you'll be able to reach Ido's birthday!"


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


if __name__ == '__main__':
    # 3.1.3
    # Call the function to execute all the functions and catch the exceptions
    execute_functions()

    # 3.2.5
    print(read_file("one_lined_file.txt"))
    print(read_file("file_does_not_exist.txt"))

    # 3.3.2
    send_invitation("John", 17)
    send_invitation("Alice", 20)
