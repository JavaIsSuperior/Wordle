from wordle_result import LetterAnalysis


class colors:
  '''Colors class:reset all colors with colors.reset; two
  sub classes fg for foreground
  and bg for background; use as colors.subclass.colorname.
  i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
  underline, reverse, strike through,
  and invisible work with the main class i.e. colors.bold'''
  reset = '\033[0m'
  bold = '\033[01m'
  disable = '\033[02m'
  underline = '\033[04m'
  reverse = '\033[07m'
  strikethrough = '\033[09m'
  invisible = '\033[08m'

  class fg:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    white = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

  class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'


# Print Pretty
def set_green(char):
  return colors.bold + colors.bg.green + colors.fg.white + " " + char + " " + colors.reset


def set_yellow(char):
  return colors.bold + colors.bg.orange + colors.fg.white + " " + char + " " + colors.reset


def set_grey(char):
  return colors.bold + colors.bg.black + colors.fg.white + " " + char + " " + colors.reset


def colored_word(word, letter_analysis):
  # Expects word and result to be of the same length
  result = ""
  for i, c in enumerate(word):
    if letter_analysis[i] == LetterAnalysis.NO_MATCH:
      result += set_grey(" " + c + " ")
    elif letter_analysis[i] == LetterAnalysis.PARTIAL_MATCH:
      result += set_yellow(" " + c + " ")
    elif letter_analysis[i] == LetterAnalysis.EXACT_MATCH:
      result += set_green(" " + c + " ")
    else:
      # This should never happen
      print("Error!")
  return result
