from src.python.pim.polynomial_representation import Polynomial


def zero_polynomial_test():
    assert Polynomial([0]).coefficients == ([])
    assert len(Polynomial([0])) == 0


f: Polynomial = Polynomial([1, 2, 3])
g: Polynomial = Polynomial([-8, 17, 0, 5])


def add_polynomial_test():
    assert (f + g).coefficients == ([-7, 19, 3, 5])


def mul_polynomial_test():
    assert (f * g).coefficients == ([-8, 1, 10, 56, 10, 15, 0])


def test_polynomial_evaluate_at():
    assert f.evaluate(2) == (1 + 4 + 12)
