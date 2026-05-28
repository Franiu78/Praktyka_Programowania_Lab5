# Exemplary calculator tests
import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected

@pytest.mark.parametrize("a, expected", [(1, 1), (2, 10), (3, 11), (4, 100)])
def test_bin(a, expected):
    result = utils.bin(a)
    assert result == expected


@pytest.mark.parametrize("a", [-1, 101, 110])
def test_bin_value_error(a):
    with pytest.raises(ValueError):
        utils.bin(a)   


@pytest.mark.parametrize("a", [0.5, 1.5, 39.5])
def test_bin_type_error(a):
    with pytest.raises(TypeError):
        utils.bin(a)
