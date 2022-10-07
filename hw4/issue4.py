import pytest
from ohe import fit_transform


def test_usual_case():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == expected


def test_exception():
    with pytest.raises(TypeError):
        fit_transform()


def test_one_city():
    assert fit_transform('Moscow') == [('Moscow', [1])]


def test_one_city_with_repetition():
    cities = ['Moscow', 'Moscow']
    exp = [
        ('Moscow', [1]),
        ('Moscow', [1])
    ]
    assert fit_transform(cities) == exp

