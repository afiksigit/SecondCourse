"""
Made by Afik
"""

import winsound
from itertools import combinations


# 5.1.2
def play_song():
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    for note in notes.split("-"):
        duration = int(note.split(",")[1])  # note duration
        frequency = freqs[note.split(",")[0]]  # note frequency
        try:
            winsound.Beep(frequency, duration)  # Play the sound
        except RuntimeError as e:
            print(f"Error playing note '{note}': {str(e)}")


# 5.2.3
def hundred_dollar_combination():
    """
    Calculates the different options to create a sum of $100 from the given bills.
    Returns:
        num_options (int): The total number of unique options to create $100 using the given bills.
    """
    # Create a list of bills
    bills = [20] * 3 + [10] * 5 + [5] * 2 + [1] * 5
    options = []

    # Generate combinations of bills
    for r in range(1, len(bills) + 1):
        for combination in combinations(bills, r):
            # Check if the sum of the combination equals $100
            if sum(combination) == 100:
                option = sorted(combination)
                options.append(option)

    # Convert options to a set to remove duplicates
    unique_options = set(map(tuple, options))

    # Print each unique option
    for option in unique_options:
        print(' '.join(str(bill) for bill in option))

    return len(unique_options)


class MusicNotes:
    def __init__(self):
        self.notes = [
            [55, 110, 220, 440, 880],
            [61.74, 123.48, 246.96, 493.92, 987.84],
            [65.41, 130.82, 261.64, 523.28, 1046.56],
            [73.42, 146.84, 293.68, 587.36, 1174.72],
            [82.41, 164.82, 329.64, 659.28, 1318.56],
            [87.31, 174.62, 349.24, 698.48, 1396.96],
            [98, 196, 392, 784, 1568]
        ]
        self.current_octave = 0
        self.current_note = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_octave >= len(self.notes[0]):
            raise StopIteration

        freq = self.notes[self.current_note][self.current_octave]

        self.current_note += 1
        if self.current_note >= len(self.notes):
            self.current_note = 0
            self.current_octave += 1

        return freq


def main():
    # 5.1.2
    play_song()

    # 5.2.2
    numbers = iter(list(range(1, 101)))
    for i in numbers:
        try:
            print(i)
            next(numbers)  # Skip the next two numbers
            next(numbers)
        except StopIteration:
            break

    # 5.2.3
    option_amount = hundred_dollar_combination()
    print(option_amount, "Options")

    # 5.3.2
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == '__main__':
    main()
