"""
Made by Afik
"""

import string

"""Validate Username methods"""


# Exception if password has illegal character
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, index):
        self.char = char
        self.index = index

    def __str__(self):
        return f"The username contains an illegal character '{self.char}' at index {self.index}"


# Exception if password too short
class UsernameTooShort(Exception):
    def __str__(self):
        return "Invalid username length. It must be more than 3 characters."


# Exception if password too long
class UsernameTooLong(Exception):
    def __str__(self):
        return "Invalid username length. It must be more than 16 characters."


"""Validate Password methods"""


# Exception if password is less than 7 characters
class PasswordTooShort(Exception):
    def __str__(self):
        return "Password must be more than 7"


# Exception if password is more than 41 characters
class PasswordTooLong(Exception):
    def __str__(self):
        return "Password must be less than 41"


# Super Exception if password Missing character
class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


# sub Exception if password Missing uppercase character
class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


# sub Exception if password Missing lowercase character
class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


# sub Exception if password Missing digit character
class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


# sub Exception if password Missing special character
class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


def check_input(username, password):
    # Check username
    if len(username) < 3:
        raise UsernameTooShort
    if len(username) > 16:
        raise UsernameTooLong
    if not all(char.isalnum() or char == '_' for char in username):
        illegal_char = next((char for char in username if not char.isalnum() and char != '_'), None)
        index = username.index(illegal_char)
        raise UsernameContainsIllegalCharacter(illegal_char, index)

    # Check password
    if len(password) < 8:
        raise PasswordTooShort
    if len(password) > 40:
        raise PasswordTooLong()
    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase
    if not any(char.islower() for char in password):
        raise PasswordMissingLowercase
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigit
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingDigit

    # If all checks pass
    print("OK")


def main():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        try:
            check_input(username, password)
            break
        except UsernameTooShort as e:
            print(e)
        except UsernameTooLong as e:
            print(e)
        except UsernameContainsIllegalCharacter as e:
            print(e)
        except PasswordTooShort as e:
            print(e)
        except PasswordTooLong as e:
            print(e)
        except PasswordMissingUppercase as e:
            print(e)
        except PasswordMissingLowercase as e:
            print(e)
        except PasswordMissingDigit as e:
            print(e)
        except PasswordMissingSpecial as e:
            print(e)


if __name__ == '__main__':
    main()
