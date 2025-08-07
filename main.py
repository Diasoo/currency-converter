import logging
from source.currency_converter import CurrencyConverter
from source.exchange_rates import ExchangeRateProvider


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    provider = ExchangeRateProvider(
        "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    )
    converter = CurrencyConverter(provider)
    print(converter.convert(100, "EUR", "CZK"))
    print(converter.convert(100, "CZK", "EUR"))
    print(converter.convert(100, "EUR", "EUR"))
    print(converter.convert(100, "EUR", "JPY"))
