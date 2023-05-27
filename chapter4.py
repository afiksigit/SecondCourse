"""
Made by Afik
"""


def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translated_sentence = ' '.join(words.get(word) for word in sentence.split())
    return translated_sentence


def first_prime_over(n):
    primes = (num for num in range(n + 1, n + 1000000) if is_prime(num))
    return next(primes)


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 4.2.2
def parse_ranges(ranges_string):
    # First generator: process the input string and yield range pairs
    range_pairs = (pair.split('-') for pair in ranges_string.split(','))

    # Second generator: yield individual numbers from the range pairs
    numbers = (num for start, stop in range_pairs for num in range(int(start), int(stop) + 1))

    return numbers


# 4.3.4
def get_fibo():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


def main():
    print(translate("el gato esta en la casa"))
    print(first_prime_over(1000000))

    # 4.2.2
    print(list(parse_ranges("1-2,4-4,8-10")))

    # 4.3.4
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))


if __name__ == '__main__':
    main()
