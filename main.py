import random
from words import word_to_guess
from visual_effect import effect
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman ():
    word = get_valid_word(word_to_guess)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:
      print(f'\nYou have {lives} lives, and these are the letters used: ', ' '.join(used_letters))

      word_list = [letter if letter in used_letters else '-' for letter in word]
      print('Current word: ', ''.join(word_list))

      user_letter = input('Guess a letter from the word: ').upper()
      if user_letter in alphabet - used_letters:
          used_letters.add(user_letter)
          if user_letter in word_letters:
              word_letters.remove(user_letter)
              print('')
          else:
              lives = lives - 1
              print('Your letter,', user_letter, 'is not in the word.')

      elif user_letter in used_letters:
          print('You already used that letter, please try another one.')
      else:
          print('Invalid character. Try again please.')

    if lives == 0:
        print(effect[lives])
        print(f'You died, the word was {word}')
    else:
        print(f'Yay, you guessed the word {word}!!') 

hangman()
