import pytest
from source.exchange_rates import ExchangeRateProvider
from source.currency_converter import CurrencyConverter


MOCK_RESPONSE = (
    "05.08.2025\n"
    "country|currency|amount|code|rate\n"
    "EMU|euro|1|EUR|25,000\n"
    "USA|dollar|1|USD|23,000\n"
    "Japan|yen|100|JPY|17,000\n"
)


@pytest.mark.parametrize(
    "amount, from_currency, to_currency, expected_rate",
    [
        (100, "EUR", "CZK", 2500.0),
        (100, "CZK", "EUR", 4.0),
        (1, "EUR", "JPY", 147.05882352941177),
        (-1, "EUR", "JPY", -147.05882352941177),
        (0, "EUR", "JPY", 0),
        (100, "EUR", "EUR", 100),
    ],
)
def test_convert(mocker, amount, from_currency, to_currency, expected_rate):
    mock_get = mocker.patch("source.exchange_rates.requests.get")
    mock_response = mocker.Mock()
    mock_response.text = MOCK_RESPONSE
    mock_response.raise_for_status = mocker.Mock()
    mock_get.return_value = mock_response

    provider = ExchangeRateProvider("dummy_url")
    converter = CurrencyConverter(provider)
    assert converter.convert(amount, from_currency, to_currency) == expected_rate
