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
