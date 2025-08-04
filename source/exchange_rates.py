import requests
import csv

def get_exchange_rates():
    r = requests.get("https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt")
    lines = r.text.splitlines()

    reader = csv.reader(lines, delimiter="|", quoting=csv.QUOTE_NONE)

    next(reader)
    next(reader)
    return reader

