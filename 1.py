import webbrowser
inp = input()
print(inp[::-1], '\nis it palindrom? ', [c for c in inp if c.isalpha()] == [c for c in inp[::-1] if c.isalpha()])
webbrowser.open(f'https://poocoo.pl/scrabble-slowa-z-liter/{inp}')
