import pytest

from core import Calculator


def test_add(calc: Calculator) -> None:
    assert calc.add() == 13


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        pytest.param(8, 3, 5, id="positive"),
        pytest.param(3, 8, -5, id="negative-result"),
        pytest.param(0, 0, 0, id="zeros"),
    ],
)
def test_subtract(left: int, right: int, expected: int) -> None:
    assert Calculator(left, right).subtract() == expected


def test_divide() -> None:
    # 浮点数比较
    assert Calculator(1, 3).divide() == pytest.approx(0.333_333, rel=1e-5)


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="right operand cannot be zero"):
        Calculator(10, 0).divide()


def test_invalid_operand() -> None:
    with pytest.raises(ValueError, match="operands must be integers"):
        Calculator("not-a-number", 2)
