from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))


print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

print(floats2[-1])
print(floats == floats2)


octets = array('B', range(6))

print(octets)

m1 = memoryview(octets)
print(m1.tolist())

m2 = m1.cast('B', [2, 3])
print(m2.tolist())

m3 = m1.cast('B', [3, 2])
print(m3.tolist())

m2[1, 1] = 22
m3[1, 1] = 33

print(octets)
