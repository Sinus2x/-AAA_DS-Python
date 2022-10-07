from what_is_year_now import what_is_year_now
from unittest.mock import MagicMock, patch
import pytest


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_usual_case(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '2019-01-01'}
    assert what_is_year_now() == 2019


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_ymd(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '2019-01-01'}
    assert what_is_year_now() == 2019


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_dmy(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '03.03.2019'}
    assert what_is_year_now() == 2019


@patch("what_is_year_now.urllib.request.urlopen")
@patch("what_is_year_now.json.load")
def test_exception(json_load_mock, openurl_mock):
    resp_mock = MagicMock()
    openurl_mock.return_value = resp_mock
    resp_mock.__enter__.return_value = resp_mock
    json_load_mock.return_value = {"currentDateTime": '03-03-2019'}
    with pytest.raises(ValueError):
        what_is_year_now()
