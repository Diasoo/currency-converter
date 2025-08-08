import argparse
from main import main
from utils.dictionary_formatter import dictionary_formatter

"""
Module currency_converter_cli.py

This script provides a command-line interface (CLI) for converting currency amounts
using the CurrencyConverter and ExchangeRateProvider classes.

Usage:
    python currency_converter_cli.py -a <amount> -f <from_currency> -t <to_currency>

Arguments:
    -a, --amount         The amount to convert (float).
    -f, --from           The source currency code (e.g., 'EUR').
    -t, --to             The target currency code (e.g., 'CZK').

Example:
    python currency_converter_cli.py -a 100 -f EUR -t CZK

Description:
    The script parses command-line arguments for the amount and currency codes,
    performs the conversion, and prints the result to the console.
"""

parser = argparse.ArgumentParser(
    prog="Currency Converter",
    description="Enter the amount and the currencies you want to convert from and to, and get the result.",
)

parser.add_argument(
    "-a", "--amount", type=float, help="Enter the amount you want to convert"
)
parser.add_argument(
    "-f",
    "--from",
    dest="from_currency",
    type=str,
    help="Enter the currency you want to convert from",
)
parser.add_argument(
    "-t", "--to", type=str, help="Enter the currency you want to convert to"
)
parser.add_argument("-l", "--list", action="store_true", help="Type -l for listing all available currencies")

args = parser.parse_args()

if args.list:
    result = main(0, "list", "list")
    print(dictionary_formatter(result))
    exit()

result = main(args.amount, args.from_currency, args.to)
print(result)
