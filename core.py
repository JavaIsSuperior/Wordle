from wordle_result import LetterAnalysis


def analyze(word, target):
  '''
    Compare the given word with the target word character by character.
    Args:
    word (str): The word to be analyzed for equivalence.
    target (str): The magic word being compared to the parameter word.
    Returns:
    dict: A dictionary where the keys are the index of the word, and each value is the result
    of whether the character in the index matches the character at the same index in the target word.
    '''
  char_is_match = LetterAnalysis.EXACT_MATCH
  char_is_in_ans = LetterAnalysis.PARTIAL_MATCH
  char_is_not_match = LetterAnalysis.NO_MATCH
  word_dict = {}
  for count, char in enumerate(word):
    if char == target[count]:
      word_dict[count] = char_is_match
    elif char in target:
      word_dict[count] = char_is_in_ans
    else:
      word_dict[count] = char_is_not_match
    target = target.replace(char, " ", 1)
  return word_dict
