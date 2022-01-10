from typing import List, Tuple
from src.python.pim.polynomial_representation import Polynomial
from src.python.pim.polynomial_representation import ZERO


def single_term(points: List[Tuple[float, float]], i: int) -> Polynomial:
    """ Return one term of an interpolated polynomial.
        Arguments:
            - points: a list of (float, float)
            - i: an integer indexing a specific point """
    the_term: Polynomial = Polynomial([1.])
    xi: float
    yi: float
    xi, yi = points[i]
    for j, p in enumerate(points):
        if j == i:
            continue
        xj: float = p[0]
        the_term: Polynomial = the_term * Polynomial([-xj / (xi - xj), 1.0 / (xi - xj)])

    return the_term * Polynomial([yi])


def interpolate(points: List[Tuple[float, float]]) -> Polynomial:
    """ Returns the unique polynomial of degree at most n passing through the given n+1 points."""
    if len(points) == 0:
        raise ValueError('Must provide at least one point.')
    x_values: List[float] = [p[0] for p in points]

    if len(set(x_values)) < len(x_values):
        raise ValueError('Not all x values are distinct.')
    terms: List[Polynomial] = [single_term(points, i) for i in range(0, len(points))]

    total_polynomial: Polynomial = ZERO

    for x in terms:
        total_polynomial: Polynomial = x + total_polynomial

    return total_polynomial
