import argparse
from exchange_rates import get_exchange_rates

parser = argparse.ArgumentParser(description="Converter between CZK and EUR")
parser.add_argument('--amount', type=float, required=True, help="Amount to be converted")
parser.add_argument('--from_to', type=str.lower, choices=['from', 'to'], required=True, help="From / To")
parser.add_argument('--currency', type=str.lower, required=True, help="Currency to be converted from/to")

args = parser.parse_args()
rates = get_exchange_rates()

for rate in rates:
    if rate[1].lower() == args.currency or rate[3].lower() == args.currency:
        if args.from_to == "from":
            res = args.amount * float(rate[4].replace(',', '.')) / float(rate[2])
            print(res)
            exit()
        elif args.from_to == "to":
            res = args.amount / float(rate[4].replace(',', '.')) * float(rate[2])
            print(res)
            exit()
        else:
            print("Invalid input")
            exit()

print("Currency was not found")