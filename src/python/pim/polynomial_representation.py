from typing import List
import re
import itertools as it
import numpy as np

class Polynomial:
    def __init__(self, coefficients: List[int]) -> None:
        self.coefficients: List[int] = coefficients

    def __str__(self) -> str:
        """returns a string representation of the polynomial"""
        coeff_list: List[str] = [display(c, i) for i, c in enumerate(self.coefficients)]
        filter_coeff_list = list(filter(lambda x: x != "", coeff_list))
        return re.sub(r"\+ -", "- ", " + ".join(filter_coeff_list))

    def __add__(self, other: Polynomial) -> Polynomial:
        """returns the sum of two polynomials (like degrees are added together)"""
        return [sum(n) for n in it.zip_longest(self.coefficients, other.coefficients, fillvalue = 0)]

    def __mul__(self, other: Polynomial) -> Polynomial:
        """returns the product of two polynomials"""
        len_self: int = len(self.coefficients)
        len_other: int = len(other.coefficients)
        blank_coeff_list: list(int) = [0] * (len_self + len_other - 1)

        #Multiplies two polynomials term by term
        for i in range(len_self):
            for j in range(len_other):
                blank_coeff_list[i + j] += self.coefficients[i] * other.coefficients[j]
        return blank_coeff_list

    def evaluate(self, value: int) -> int:
        """evaluates a polynomial at a given value"""
        calculate_list: list[str] = [calculate(c, i) for i, c in enumerate(self.coefficients)]
        total: int = 0
        for i in range(len(self.coefficients)):
            total += calculate_list[i][0] * (value ** calculate_list[i][1])
        return total

def display(coefficient: int, index: int) -> str:
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

def calculate(coefficient: int, index: int) -> (int, int):
    if coefficient == 0:
        x: int = 0
        y: int = 0
    else:
        x: int = coefficient
        y: int = index

    return (x, y)
