import argparse
from exchange_rates import get_exchange_rates

parser = argparse.ArgumentParser(description="Converter between CZK and EUR")
parser.add_argument("-a", "--amount", type=float, help="Amount to be converted")
parser.add_argument(
    "-d",
    "--direction",
    type=str.lower,
    choices=["from", "to"],
    help="From / To",
)
parser.add_argument(
    "-c",
    "--currency",
    type=str.lower,
    help="Currency to be converted from/to",
)
parser.add_argument(
    "-l", "--list", action="store_true", help="List all supported currencies"
)

args = parser.parse_args()
rates = get_exchange_rates()

if rates is None:
    print("Failed to fetch exchange rates. Please check your network connection.")
    exit(1)

if args.list:
    for rate in rates:
        print(f"{rate[1]} {rate[3]}")
    exit()

for rate in rates:
    if rate[1].lower() == args.currency or rate[3].lower() == args.currency:
        if args.direction == "from":
            res = args.amount * float(rate[4].replace(",", ".")) / float(rate[2])
            print(f"Converted value: {res:.2f} {rate[3]}")
            exit()
        elif args.direction == "to":
            res = args.amount / float(rate[4].replace(",", ".")) * float(rate[2])
            print(f"Converted value: {res}")
            exit()
        else:
            print("Invalid input")
            exit()

print("Currency was not found")
