"""Test"""
import pytest
from operations.hypotenuse import hypotenuse


@pytest.mark.parametrize(
    "cat1,cat2,exp",
    [
        (3, 4, 5),
        (2, 3, hypotenuse(2, 3)),
        (12, 4, hypotenuse(12, 4)),
        (3, 45, hypotenuse(3, 45)),
        (23, 36, hypotenuse(23, 36))
    ]
)
def test_hypotenuse_expected(cat1, cat2, exp):
    """Hypotenuse's function test"""
    assert hypotenuse(cat1, cat2) == exp
