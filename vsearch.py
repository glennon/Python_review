def search4vowels(word):
  """Display any vowels found in an input word """
  vowels = set('aeiou')
  found = sorted(vowels.intersection(set(word)))
  return bool(found)
