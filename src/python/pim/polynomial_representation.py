from typing import List, Iterator
from collections import namedtuple
import re
import itertools as it

class Polynomial(object):
    def __init__(self, coefficients: List[float]) -> None:
        """The list of coefficients includes 0 coefficients for the polynomial.
        For example, Polynomial([1, 2, 0, 3]) would represent 1 + 2x + 0x^2 + 3x^3"""
        self.coefficients: List[float] = coefficients

    def __str__(self) -> str:
        """returns a string representation of the polynomial"""
        coeff_list: List[str] = [Polynomial.display(c, i) for i, c in enumerate(self.coefficients)]
        filter_coeff_list = list(filter(lambda x: x != "", coeff_list))
        return re.sub(r"\+ -", "- ", " + ".join(filter_coeff_list))

    def __add__(self, other: "Polynomial") -> "Polynomial":
        """returns the sum of two polynomials (like degrees are added together)"""
        return Polynomial([sum(n) for n in it.zip_longest(self.coefficients, other.coefficients, fillvalue = 0)])

    def __mul__(self, other: "Polynomial") -> "Polynomial":
        """returns the product of two polynomials
        - If 𝑓 is a degree 𝑛 polynomial and 𝑔 is a degree 𝑚 polynomial then their product 𝑓⋅𝑔 is a degree 𝑛+𝑚 polynomial
        - If 𝑓 or 𝑔 are a zero polynomial, their product 𝑓⋅𝑔 is a degree 𝑚 polynomial
        (convention that a zero polynomial has a degree of 0)
        """
        if Polynomial.evaluate(self, 1) == 0:
            # if a degree 0 polynomial, any evaluation value will result in 0
            degree_self: int = 0
        else:
            degree_self: int = len(self.coefficients)

        if Polynomial.evaluate(self, 1) == 0:
            # if a degree 0 polynomial, any evaluation value will result in 0
            degree_other: int = 0
        else:
            degree_other: int = len(other.coefficients)
        # create a placeholder list of length n+m
        coeff_list: list[float] = [0] * (degree_self + degree_other)

        # Multiplies two polynomials term by term
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                coeff_list[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(coeff_list)

    def evaluate(self, value: int) -> int:
        """evaluates a polynomial at a given value"""
        polyterm_list: list[PolyTerm] = [Polynomial.create_polyterm(c, i) for i, c in enumerate(self.coefficients)]
        total: int = 0
        for i in range(len(self.coefficients)):
            total += polyterm_list[i].coefficient * (value ** polyterm_list[i].order)
        return total

    @staticmethod
    def display(coefficient: float, index: int) -> str:
        if index == 0:
            x: str = ""
        elif index == 1:
            x: str = "x"
        else:
            x: str = "x^"+str(index)
        if coefficient == 0:
            output: str = ""
        else:
            output: str = str(coefficient) + x

        return output

    @staticmethod
    def create_polyterm(coefficient: int, index: int) -> "PolyTerm":
        if coefficient == 0:
            return PolyTerm(0, 0)
        else:
            return PolyTerm(coefficient, index)

    def __iter__(self) -> Iterator[float]:
        return iter(self.coefficients)


PolyTerm = namedtuple("PolyTerm", ["coefficient", "order"])
ZERO: Polynomial = Polynomial([])
