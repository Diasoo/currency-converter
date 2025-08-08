import logging
from source.currency_converter import CurrencyConverter
from source.exchange_rates import ExchangeRateProvider


def main(amount: float, from_currency: str, to_currency: str) -> float | dict[str, str]:
    logging.basicConfig(level=logging.INFO)
    provider = ExchangeRateProvider(
        "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    )
    converter = CurrencyConverter(provider)
    if from_currency == "list":
        return provider.list_available_currencies()
    return converter.convert(amount, from_currency, to_currency)
