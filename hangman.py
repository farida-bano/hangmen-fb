# hangman.py
import random
from words import words  # importing the list of words
from hangman_visual import lives_visual_dict  # importing the visual stages
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'You have {lives} lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        # Check for valid input (only one letter)
        if len(user_letter) != 1 or user_letter not in alphabet:
            print('\nPlease enter a valid single letter.')
            continue

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f'\nGood job! The letter {user_letter} is in the word.')

            else:
                lives -= 1  # takes away a life if wrong
                print(f'\nYour letter, {user_letter}, is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f'You died, sorry. The word was {word}.')
    else:
        print(f'YAY! You guessed the word {word}!!')


if __name__ == '__main__':
    hangman()
