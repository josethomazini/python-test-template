'''
Tests for the calc module.
'''

import pytest

from sources.core import calc
from sources.core.exceptions import DivByZeroException

# Turn off linter hint because of the fixture's sintaxe.
# pylint: disable=redefined-outer-name

@pytest.fixture
def eleven():
    return 11

@pytest.mark.parametrize('n1, n2, res', [
    (1, 2, 3),
    (4, 5, 9),
    (10, 11, 21),
    (22, 23, 45),
])
def test_param_adds(n1, n2, res):
    result = calc.add(n1, n2)
    assert result == res

def test_sub():
    result = calc.sub(10, 3)
    assert result == 7

def test_add(eleven):
    result = calc.add(eleven, 12)
    assert result == 23

def test_div():
    result = calc.div(10, 2)
    assert result == 5

def test_mul():
    result = calc.mul(2, 6)
    assert result == 12

def test_div_by_0(eleven):
    with pytest.raises(DivByZeroException):
        calc.div(eleven, 0)
