from dataclasses import dataclass, field
from typing import NamedTuple, ClassVar, Optional
from enum import Enum, auto
from datetime import date


class CoordinateA(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'

        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass(frozen=True)
class CoordinateB:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


class CoordinateC(NamedTuple):
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


@dataclass()
class DemoDataClass():
    a: int
    b: float = 1.1
    c = 'spam'


class Coordinate(NamedTuple):
    """
    Provides location infromation.
    """

    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'

        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)


@dataclass
class HackerClubMember(ClubMember):
    all_handles: ClassVar[set[str]] = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__

        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle!r} already exists.'

            raise ValueError(msg)

        cls.all_handles.add(self.handle)


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """Media resource description."""

    identifier: str
    title: str = '<undefined>'
    creators: list[str] = field(default_factory=list)
    date: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = ' ' * 4
        res = [f'{cls_name}(']

        for f in fields(cls):
            value = getattr(self, f.name)
            res.append(f'{indent}{f.name} = {value!r},')

        res.append(')')
        return '\n'.join(res)
