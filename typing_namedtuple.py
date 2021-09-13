from dataclasses import dataclass, field
from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'

        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = 'WGS84'


class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'


class DemoNTClass(NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'


@dataclass()
class DemoDataClass():
    a: int
    b: float = 1.1
    c = 'spam'


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
