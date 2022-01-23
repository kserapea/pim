from typing import List, Dict
from dataclasses import dataclass, field
from functools import reduce

from src.python.pim.interpolate import interpolate
from src.python.pim.polynomial_representation import Polynomial


def run() -> None:
    f: Polynomial = Polynomial([1, 2, 3])
    g: Polynomial = Polynomial([-8, 17, 0, 5])
    h: Polynomial = f + g
    j: Polynomial = f * g

    print(f)
    print(g)
    print(h)
    print(j)

    print(Polynomial.evaluate(f, 4))

    points1 = [(1, 1)]
    points2 = [(1, 1), (2, 0)]
    points3 = [(1, 1), (2, 4), (7, 9)]
    print(interpolate(points1))
    print(interpolate(points2))
    print(interpolate(points3))


if __name__ == "__main__":
    run()
