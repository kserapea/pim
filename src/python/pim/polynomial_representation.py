from typing import List, Iterator
from collections import namedtuple
import re
import itertools as it
import numpy as np

class Polynomial(object):
    def __init__(self, coefficients: List[float]) -> None:
        """The list of coefficients includes 0 coefficients for the polynomial.
        For example, Polynomial([1, 2, 0, 3]) would represent 1 + 2x + 0x^2 + 3x^3"""
        self.coefficients: List[float] = coefficients
        self.degree: int = self.find_degree()

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
        if Polynomial.find_degree(self) == -1:
            degree_self: int = 0
        else:
            degree_self: int = Polynomial.find_degree(self)

        if Polynomial.find_degree(other) == -1:
            degree_other: int = 0
        else:
            degree_other: int = Polynomial.find_degree(other)
        # create a placeholder list of length n+m
        coeff_list: list[float] = [0] * (degree_self + degree_other)

        # Multiplies two polynomials term by term
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                coeff_list[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(coeff_list)

    def find_degree(self) -> int:
        # remove all trailing zeros
        trimmed_coeff_list: List[float] = np.trim_zeros(self.coefficients, 'b')
        # calculate length of list
        trimmed_coeff_list_length: int = len(trimmed_coeff_list)
        # if list is now empty, means all values were 0; using -1 as a symbol of a zero polynomial
        if trimmed_coeff_list_length == 0:
            return -1
        else:
            # otherwise, the length should = the largest index for a non-zero value
            return trimmed_coeff_list_length

        # I had written a loop for that, which really does the same thing, but is not necessary with the trimmed list
        # for x in range(trimmed_coeff_list_length, 0, -1):
        #        if x != 0:
        #           return trimmed_coeff_list.index(x) """

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
