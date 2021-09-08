fp = open('cafe.txt', 'w', encoding='utf_8').write('café')
text = open('cafe.txt').read()

print(text)
