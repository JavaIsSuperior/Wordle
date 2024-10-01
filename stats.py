class Statistics:
  '''
  This file contains a class that calculates and prints statistics related to the Wordle game that will be played

  Returns:
  A total amount of games, differing between those woon and lost, a guess distribution and win percentage number, and the amount of average guesses
  '''

  def __init__(self):
    self.games_lost = 0
    self.games_won = 0
    self.guess_dist = {i: 0 for i in range(1, 7)}
    self.total_guesses_won = 0
    self.win_streak = 0
    self.max_win_streak = []

  def add_lost_game(self):
    self.games_lost += 1
    self.win_streak = 0

  def add_won_game(self, num_guesses):
    self.games_won += 1
    self.win_streak += 1
    if len(self.max_win_streak) < self.win_streak:
      self.max_win_streak += 'w'
    self.guess_dist[num_guesses] += 1
    self.total_guesses_won += num_guesses

  def get_guess_distribution(self):
    self.total_games = self.games_lost + self.games_won
    guess_distrubtion = {}
    for key, value in self.guess_dist.items():
      if self.total_games > 0:
        guess_distrubtion[key] = value / self.total_games
      else:
        guess_distrubtion[key] = 0
    return guess_distrubtion

  def get_success_metrics(self):
    self.total_games = self.games_won + self.games_lost
    win_fraction = (self.games_won /
                    self.total_games if self.total_games > 0 else 0)
    avg_guesses = (self.total_guesses_won /
                   self.games_won if self.games_won > 0 else 0)
    return win_fraction, avg_guesses

  def print_stats(self):
    print(f"{'='*30}")
    print(f"{'Games Statistics:'.center(30, ' ')}")
    print(f"{'='*30}")
    print(f"Total games played: {self.games_won + self.games_lost}")
    print(f"Games won: {self.games_won}")
    print(f"Games lost: {self.games_lost}")
    print(f"Win streak: {self.win_streak}")
    print(f"Max win streak: {len(self.max_win_streak)}")
    print(f"{'='*30}")
    print(f"{'Guess Distribution:'.center(30, ' ')}")
    guess_distrubtion = self.get_guess_distribution()
    for guess, fraction in guess_distrubtion.items():
      print(f"Guesses: {guess}, Win Fraction: {fraction:.2f}")
    win_fraction, avg_guesses = self.get_success_metrics()
    print(f"Win Fraction: {win_fraction*100:.0f}%")
    print(f"Average Guesses to Win: {avg_guesses:.2f}")
    print(f"{'='*30}")
