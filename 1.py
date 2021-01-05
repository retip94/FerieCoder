import webbrowser
inp = input()
print(inp[::-1], '\nis it palindrom? ', [c for c in inp.lower() if c.isalpha()] == [c for c in inp[::-1].lower() if c.isalpha()])
webbrowser.open(f'https://poocoo.pl/scrabble-slowa-z-liter/{inp}')