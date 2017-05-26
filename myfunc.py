def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()
    else:
        print('no inputs')
