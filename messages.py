from typing import Optional, Union, Any, NamedTuple, TypeVar
from geolib import geohash as gh  # type: ignore
from collections.abc import Sequence, Iterator, Mapping, Iterable  # type: ignore
import sys
import re
import unicodedata
from random import shuffle
from collections import Counter
from decimal import Decimal
from fractions import Fraction

PRECISION = 9
RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1


def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f'1 {singular}'

    count_str = str(count) if count else 'no'

    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}s'


def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token


def tokenize(text: str) -> list[str]:
    return text.upper().split()


def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)


class Coordinate(NamedTuple):
    lat: float
    lon: float


def geohash_2(lat_lon: Coordinate) -> str:
    return gh.encode(*lat_lon, PRECISION)


def columnize(
    sequence: Sequence[str], num_columns: int = 0
) -> list[tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence) ** 0.5)
    num_rows, reminder = divmod(len(sequence), num_columns)
    num_rows += bool(reminder)
    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]


def tokenize_2(text: str) -> Iterator[str]:
    """return iterable of uppercase words"""
    for match in RE_WORD.finditer(text):
        yield match.group().upper()


def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}

    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index


def name2hex(name: str, color_map: Mapping[str, int]) -> str:
    pass


FromTo = tuple[str, str]


def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)

    return text


T = TypeVar('T')


def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError('size must be >= 1')

    result = list(population)
    shuffle(result)
    return result[:size]


def mode(data: Iterable[float]) -> float:
    pairs = Counter(data).most_common(1)

    if len(pairs) == 0:
        raise ValueError('node mode for empty data')

    return pairs[0][0]


NumberT = TypeError('NumberT', float, Decimal, Fraction)


def mode_1(data: Iterable[NumberT]) -> NumberT:
    pass
