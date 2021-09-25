import contextlib

try:
    1/10
except ZeroDivisionError:
    print("caught divide-by-0 attempt")

f = open(some_file, 'w')

try:
    do_something(f)
finally:
    f.close()

  equal

with open(some_file, 'w') as f:
    do_something(f)


class tag(object):
    def __init__(self, tagname):
        self.tagname = tagname

    def __enter__(self):
        print('<{}>'.format(self.tagname), end='')

    def __exit__(self, etyp, einst, etb):
        print('</{}>'.format(self.tagname))

@contextlib.contextmanager
def tag(tagname):
    print('<{}>'.format(tagname), end='')

    try:
        yield
    finally:
        print('</{}>'.format(tagname))


tt = tag('sometag')

class InvalidAttribute(AttributeError):
    """Used to indicate attributes that could never be valid"""


class SomeFunkyClass(object):
    """much hypothetical functionality snipped"""

    def __getattr__(self, name):
        """only clarifies the kind of attribute error"""

        if name.startswith('_'):
            raise InvalidAttribute, 'Unknown private attribute ' + name
        else:
            raise AttributeError, 'Unknown attribute ' + name
