from source.exchange_rates import ExchangeRateProvider


class CurrencyConverter:
    """
    A class for converting currencies using an exchange rate provider.

    Attributes:
        rate_provider (ExchangeRateProvider): An instance of the exchange rate provider.

    Methods:
        convert(amount: float, from_currency: str, to_currency: str) -> float:
            Converts the specified amount from one currency to another.
    """

    def __init__(self, rate_provider: ExchangeRateProvider) -> None:
        self.rate_provider: ExchangeRateProvider = rate_provider

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        rate: float = self.rate_provider.get_rate(from_currency, to_currency)
        return amount * rate
