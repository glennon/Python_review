def search4vowels(word):
  """Display any vowels found in an input word """
  vowels = set('aeiou')
  return vowels.intersection(set(word))
