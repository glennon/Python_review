def search4vowels(phrase:str) -> set:
  """Display any vowels found in an input word """
  vowels = set('aeiou')
  return vowels.intersection(set(phrase))

def search4letters(phrase:str='the quick brown fox jumped over the lazy dog', letters:str='aeiou') -> set:
  """Display any 'letters' found in an input word """
  return set(letters).intersection(set(phrase))
