import random
from stats import Statistics
from core import analyze
import coloring
from coloring import colored_word


def run_game(file_name, inputs=None):
  '''
  Start a game by using the dictionary and guesses provided
  Returns: A boolean and a string
  '''
  stats = Statistics()
  with open(file_name, 'r') as file:
    words = [word.strip().upper() for word in file.readlines()]
  while True:
    guesses = []
    chosen_word = random.choice(words)
    num_attempts = 0
    guessed = False
    input_ite = iter(inputs) if inputs else None
    while num_attempts < 6:
      if input_ite:
        word = next(input_ite)
      else:
        print(f"{'='*30}")
        word = input("Enter a 5 letter word: ").upper() if not inputs else None
        if word is not None:
          if word in words and len(word) == 5:
            word_dict = analyze(word, chosen_word)
            result = colored_word(word, word_dict)
            guesses.append(result)
            print()
            for i in guesses:
              print(i)
            if word == chosen_word:
              print()
              print("Congratulations, you won!")
              guessed = True
              stats.add_won_game(num_attempts + 1)
              break
            else:
              guess_list = [i for i in word if i in chosen_word]
              probable_ans = words[:]
              if len(guess_list) > 0:
                for i in guess_list:
                  probable_ans = [word for word in probable_ans if i in word]

                print()
                print(
                    f"These are your possible answers: {', '.join(probable_ans)}"
                )
              num_attempts += 1
              print()
            print(f"You have {6 - num_attempts} guesses left")
          else:
            print(f"{'='*30}")
            if len(word) != 5:
              print("Invalid word length, try again")
            elif word not in words:
              print("Invalid word, not in dictionary, try again")
    if not guessed:
      print()
      print(f"Out of attempts, you have lost. The word was {chosen_word}")
      stats.add_lost_game()
    stats.print_stats()
    play_again = input(
        "Do you want to play again? (y/n): ").lower() if not inputs else None
    if play_again != 'y':
      break
