from collections import abc
print(issubclass(tuple, abc.Sequence))
print(issubclass(tuple, abc.MutableSequence))
print(issubclass(list, abc.MutableSequence))

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]


x = 'ABC'

codes = [ord(x) for x in x]
codes = [last := ord(c) for c in x]
print("-=-=-=")
print(last)
print(codes)

colors = ['balck', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for size in sizes
           for color in colors]

print(tshirts)
