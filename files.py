import json
with open('example.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())

filename = 'example.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

stripped_text = ''

for line in lines:
    stripped_text += line.rstrip()

print(stripped_text[:21])
print('3.14' in stripped_text)

numbers = [1, 2, 3, 4, 5, 6]

with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers = json.load(f)
