import pytest

from core import Calculator


# Test functions can directly use fixture names as input arguments in which case the fixture instance returned from the fixture function will be injected.
@pytest.fixture
def calc() -> Calculator:
    return Calculator(10, 3)


@pytest.fixture
def add_result(calc):
    return calc.add()