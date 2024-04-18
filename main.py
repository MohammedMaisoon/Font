font_dict = {
    'A': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
    'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
    'C': [' *** ', '*   *', '*    ', '*   *', ' *** ']
}
def print_text(text):
    for i in range(5):
        for char in text:
            print(font_dict[char.upper()][i], end='  ')
        print()
print_text('ABC')

