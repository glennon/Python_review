phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.remove('D')
plist.insert(4, 'a')
plist = plist[:7]
plist.remove(' ')
plist.remove("'")
plist.insert(2, ' ')

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
