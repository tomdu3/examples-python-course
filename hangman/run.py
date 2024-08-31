"""Hangman Game"""

import random

# word list from a file
# word_list = [
#    "apple",
#    "banana",
#    "orange",
#    "pear",
#    "strawberry",
#    "watermelon",
# ]

word_list = []
with open("wordslist.txt") as f:
    for word in f.readlines():
        word_list.append(word.strip())


HANGMANPICS = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def word_display(word, guessed_letters=[]):
    """
    Displays a word in underscores except for the guessed letters
    """
    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print()


def check_guess(guessed_letter, word):
    """
    Returns true if the guessed letter is in the word
    """
    if guessed_letter in word:
        return True
    else:
        return False


def user_guess():
    while True:
        letter = input("Guess a letter: ").lower().strip()
        if len(letter) > 1:
            print("only one letter, please!")
        elif not letter.isalpha():
            print("only letters please!")
        else:
            return letter


def display_hangman(wrong_letters_count):
    print(HANGMANPICS[wrong_letters_count - 1])


def game():
    wrong_letters_count = 0
    guessed_letters = []
    typed_letters = []
    word = random.choice(word_list)
    # print(word)  # cheating

    print()
    # display initial word with underscores
    word_display(word)
    print()
    while True:
        guess = user_guess()  # guess a letter
        if guess in typed_letters:
            print("Letter already tried. Please try again.")
            continue
        else:
            typed_letters.append(guess)

            if check_guess(guess, word):  # check if the letter is in the word
                guessed_letters.append(guess)
                word_display(word, guessed_letters)
                if len(guessed_letters) == len(set(word)):  # if all letters guessed
                    print("You win!")
                    return
            else:
                wrong_letters_count += 1
                display_hangman(wrong_letters_count)
                if wrong_letters_count == 7:
                    print("Wrong guess! You lose!")
                    return
                print("Wrong guess!")
                word_display(word, guessed_letters)


game()
