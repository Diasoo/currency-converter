import pytest
from source.exchange_rates import ExchangeRateProvider


MOCK_RESPONSE = (
    "05.08.2025\n"
    "country|currency|amount|code|rate\n"
    "EMU|euro|1|EUR|25,000\n"
    "USA|dollar|1|USD|23,000\n"
    "Japan|yen|100|JPY|17,000\n"
)


def test_fetch_rate(mocker):
    mock_get = mocker.patch("source.exchange_rates.requests.get")
    mock_response = mocker.Mock()
    mock_response.text = MOCK_RESPONSE
    mock_response.raise_for_status = mocker.Mock()
    mock_get.return_value = mock_response

    provider = ExchangeRateProvider("dummy_url")
    assert provider.rates["EUR"] == 25.0
    assert provider.rates["USD"] == 23.0
    assert provider.rates["JPY"] == 0.17
    with pytest.raises(ValueError, match="Currency not found:"):
        provider.get_rate("dummy", "dummy")
    with pytest.raises(ValueError, match="Currency not found:"):
        provider.get_rate("", "")


def test_format_rate():
    provider = ExchangeRateProvider("dummy_url")
    assert provider.format_rate("25.123") == 25.123
    assert provider.format_rate("1") == 1.0


@pytest.mark.parametrize(
    "from_currency, to_currency, expected_rate",
    [("CZK", "EUR", 25.0), ("EUR", "CZK", 1 / 25.0), ("USD", "EUR", 23.0 / 25.0)],
)
def test_get_rate(mocker, from_currency, to_currency, expected_rate):
    mock_get = mocker.patch("source.exchange_rates.requests.get")
    mock_response = mocker.Mock()
    mock_response.text = MOCK_RESPONSE
    mock_response.raise_for_status = mocker.Mock()
    mock_get.return_value = mock_response

    provider = ExchangeRateProvider("dummy_url")
    assert provider.get_rate(from_currency, to_currency) == expected_rate
