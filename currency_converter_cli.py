import argparse
from main import main


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
args = parser.parse_args()

result = main(args.amount, args.from_currency, args.to)
print(result)
