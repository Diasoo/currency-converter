from typing import Iterator
import requests
import csv
import logging


class ExchangeRateProvider:
    """
    Provides exchange rate data by fetching and parsing rates from a specified source URL.

    This class retrieves exchange rates (typically from a CSV or pipe-delimited source), parses them,
    and allows conversion between different currencies using the fetched rates.

    Attributes:
        source_url (str): The URL from which to fetch exchange rate data.
        rates (dict[str, float]): A mapping from currency codes to their exchange rates.

    Methods:
        fetch_rate(): Fetches and parses the exchange rates from the source URL.
        get_rate(from_currency: str, to_currency: str) -> float: Returns the exchange rate from one currency to another.
        format_rate(rate: str) -> float: Converts a rate string to a float.
    """

    def __init__(self, source_url: str) -> None:
        self.source_url: str = source_url
        self.rates: dict[str, float] = {}
        self.available_currencies: dict[str, str] = {}
        self.fetch_rate()

    def fetch_rate(self) -> bool:
        try:
            r: requests.Response = requests.get(self.source_url)
            r.raise_for_status()
            logging.info("Fetching was successful")
        except requests.exceptions.RequestException as e:
            logging.error(f"Network error while fetching exchange rates: {e}")
            return False
        lines: list[str] = r.text.splitlines()
        reader: Iterator[list[str]] = csv.reader(
            lines, delimiter="|", quoting=csv.QUOTE_NONE
        )
        next(reader)
        next(reader)
        for line in reader:
            unit: int = int(line[2])
            self.available_currencies[line[1]] = line[3]
            self.rates[line[3]] = self.format_rate(line[4]) / unit
        return True

    def get_rate(self, from_currency: str, to_currency: str) -> float:
        try:
            if from_currency == "CZK":
                return self.rates[to_currency]
            elif to_currency == "CZK":
                return 1 / self.rates[from_currency]
            else:
                return self.rates[from_currency] / self.rates[to_currency]
        except KeyError:
            raise ValueError(f"Currency not found: {from_currency} or {to_currency}")

    def list_available_currencies(self) -> dict[str, str]:
        return self.available_currencies

    def format_rate(self, rate: str) -> float:
        return float(rate.replace(",", "."))

    def __str__(self) -> str:
        return f"Exchange rates from: {self.source_url}"
