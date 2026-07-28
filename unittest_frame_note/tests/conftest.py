import pytest

from core import Calculator


@pytest.fixture
def calc() -> Calculator:
    return Calculator(10, 3)
