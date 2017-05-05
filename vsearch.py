def search4vowels(phrase:str) -> set:
  """Display any vowels found in an input word """
  vowels = set('aeiou')
  return vowels.intersection(set(phrase))
