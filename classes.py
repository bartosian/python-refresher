import collections


class Base(object):
    def greet(self, name): print('Welcome', name)


class Sub(Base):
    def greet(self, name):
        print('Well Met and', end=' ')
        Base.greet(self, name)


x = Sub()
x.greet('Alex')


class Base(object):
    def __init__(self):
        self.anattribute = 23


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.anotherattribute = 45


class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


class Singleton(object):
    _singletons = {}

    def __new__(cls, *args, **kwds):
        if cls not in cls._singletons:
            cls._singletons[cls] = super(Singleton, cls).__new__(cls)

        return cls._singletons[cls]


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    area = property(fget=get_area, doc='area of rectangle')


class Rectangle(object):
    __slots__ = 'width', 'height'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        '''area of the rectangle'''
        return self.width * self.height

    @area.setter
    def area(self, value):
        scale = math.sqrt(value/self.area)
        self.width *= scale
        self.height *= scale
