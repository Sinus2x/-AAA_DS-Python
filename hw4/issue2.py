from issue1 import decode
import pytest


@pytest.mark.parametrize(
    "source_string,result",
    [
        ('... --- ...', 'SOS'),
        ('... ---', 'SO'),
        ('.... ..', 'HI')
    ]
)
def test_decode(source_string, result):
    assert decode(source_string) == result
