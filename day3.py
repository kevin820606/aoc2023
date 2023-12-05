from code import interact
from dataclasses import dataclass, field
import math
import typing
import utils

quiz = utils.read_quiz(3)


class Coord(typing.NamedTuple):
    x: int
    y: int


@dataclass
class Number:
    number: int
    location: list[Coord]
    surround: set[Coord] = field(init=False)

    def __post_init__(self) -> None:
        self.surround = set()
        for loc in self.location:
            self.surround.update(
                [
                    Coord(x=loc.x + 1, y=loc.y),
                    Coord(x=loc.x, y=loc.y + 1),
                    Coord(x=loc.x - 1, y=loc.y),
                    Coord(x=loc.x, y=loc.y - 1),
                    Coord(x=loc.x + 1, y=loc.y + 1),
                    Coord(x=loc.x + 1, y=loc.y - 1),
                    Coord(x=loc.x - 1, y=loc.y - 1),
                    Coord(x=loc.x - 1, y=loc.y + 1),
                ]
            )


number_str = ""
nloc = []
numbers: list[Number] = []
strange_sign: set[Coord] = set()
possible_gear: set[Coord] = set()
for ln, line in enumerate(quiz):
    for wn, word in enumerate(line.strip()):
        if word.isdigit():
            number_str += word
            nloc.append(Coord(x=wn, y=ln))
        else:
            if number_str:
                numbers.append(Number(number=int(number_str), location=nloc))
                number_str = ""
                nloc = []
            if word != ".":
                strange_sign.add(Coord(x=wn, y=ln))
            if word == "*":
                possible_gear.add(Coord(x=wn, y=ln))

no_in_n = []
for number in numbers:
    if number.surround.intersection(strange_sign):
        no_in_n.append(number.number)
print(sum(no_in_n))


gears: dict[Coord, list[int]] = {}
for pgear in possible_gear:
    gears[pgear] = []
    for number in numbers:
        if pgear in number.surround:
            gears[pgear].append(number.number)
    if len(gears[pgear]) != 2:
        gears.pop(pgear)
print(sum(map(math.prod, gears.values())))
