def search4vowels():
  """Display any vowels found in an input word """
  vowels = set('aeiou')
  word = input('Provide a word to search for vowels: ')
  found = sorted(vowels.intersection(set(word)))
  for vowel in found:
    print(vowel)
