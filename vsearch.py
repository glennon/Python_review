def search4vowels(word:str) -> set:
  """Display any vowels found in an input word """
  vowels = set('aeiou')
  return vowels.intersection(set(word))
