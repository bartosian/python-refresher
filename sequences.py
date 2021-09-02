import array
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

symbols_1 = tuple(ord(symbol) for symbol in symbols)
print(symbols_1)

symbols_2 = array.array('I', (ord(symbol) for symbol in symbols))
print(symbols_2)

for tshirt in (f'{c} {s}' for c in colors
               for s in sizes):
    print(tshirt)

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)

traveler_ids = [('USA', '3119855'), ('BRA', '2809855')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(a == b)

b[-1].append(99)

print(a == b)


def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True


tf = (10, 'alpha', (1, 2))
tm = (10, 'alpha', [1, 2])

print(fixed(tf))
print(fixed(tm))

a = [1, 2, 3]
b = [4, 5, 6]
c = (1, 2, 3)
d = (4, 5, 6)

lax_coordinates = (33.9, -118.408)
latitude, longitiude = lax_coordinates

a = 1
b = 2

a, b = b, a

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')

    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == '__main__':
    main()
