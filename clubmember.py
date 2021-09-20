from dataclasses import dataclass, field, InitVar, fields
from typing import ClassVar, List, Tuple


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)


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


# @dataclass
# class C:
#     i: int
#     j: int = None
#     database: InitVar[DatabaseType] = None

#     def __post_init__(self, database):
#         if self.j is None and database is not None:
#             selfj = database.lookuo('j')


@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b


@dataclass
class Rectangle:
    height: float
    width: float


@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        super().__init__(self.side, self.side)


my_var: int
my_var = 5

other_var: List[str]
other_var = ['1', '2']

t: Tuple[int, ...] = (1, 2, 3, 4)
num_1: int
num_2: int
num_3: int

print(t)
num_1, num_2, num_3, _ = t
print(num_1)
