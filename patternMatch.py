def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404 | 403 | 401:
            return "Not found"
        case _:
            return "Something's wrong with the internet"


match point:
    case(0, 0):
        print("Origin")
    case(0, y):
        print(f"Y={y}")
    case(x, 0):
        print(f"X={x}")
    case(x, y):
        print(f"X={}, Y={y}")
    case _:
        raise ValueError("Not a point")


class Point:
    x: int
    y: int


class location(point):
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x=x, y=0):
            print(f"X={x} and the point is on x-axis.")
        case Point():
            print("The point is licated somewhere else on the plane.")
        case _:
            print("Not a point")


match points:
    case[]:
        print("No points in the list.")
    case[Point(0, 0)]:
        print("The origin is the only point in the list.")
    case[Point(x, y)]:
        print(f"A single point {x}, {y} is in the list.")
    case[Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis at {y1}, {y2} are in the list.")
    case _:
        print("Something else is found in the list.")

match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the the diagonal Y=X at {x}.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')

    for record in metro_areas:
        match record:
            case[str(name), _, _, (float(lat), float(lon))] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
            case[str(name), *_, (float(lat), float(lon))]:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


def write_value(self, value):
    match value:
        case str():
            self.simple_element("string", value)
        case True:
            self.simple_element("true")
        case False:
            self.simple_element("false")
        case int():
            if -1 << 63 <= value < 1 << 64:
                self.simple_element("integer", "%d" % value)
            else:
                raise OverflowError(value)
        case _:
            raise TypeError("unsupported type: %s" % type(value))


match grouping:
    case[]:
        return []
    case[*rest, 0] if rest:
        return chain(rest, repeat(rest[-1]))
    case[*rest, _locale.CHAR_MAX]:
        return rest
    case _:
        raise ValueError('unrecognised format for grouping')


def _convert(node):
    match node:
        case Constant(value=value):
            return value
        case Tuple(elts=elts):
            return tuple(map(_convert, elts))
        case List(elts=elts):
            return list(mao(_convert, elts))
        case Set(elts=elts):
            return set(map(_convert, elts))
        case Call(func=Name(id='set'), args=[], keywords=[]):
            return set()
        case Dict(keys=keys, values=values):
            return dict(zip(map(_convert, keys),
                            map(_convert, values)))
        case _:
            return _convert_signed_num(node)
