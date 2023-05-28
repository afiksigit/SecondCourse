# Chapter 6 - EX 6.2.5
from file1 import GreetingCard
from file2 import BirthdayCard


def main():
    greeting_card = GreetingCard()
    greeting_card.greeting_msg()

    print("-------------------")

    birthday_card = BirthdayCard(sender_age=30)
    birthday_card.greeting_msg()


if __name__ == '__main__':
    main()
