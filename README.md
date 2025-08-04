# CLI měnový převodník (CZK)

Jednoduchý nástroj v Pythonu pro převod mezi CZK a vybranými cizími měnami.  
Kurzy jsou stahovány z denního kurzovního lístku České národní banky.

## Použití

```bash
python converter.py --amount 100 --from_to from --currency eur
```

--amount – částka k převodu
--from_to – směr převodu: from (z měny do CZK) nebo to (z CZK do měny)
--currency – kód měny podle ČNB (např. eur, usd, jpy)

## Závislosti
Python 3.8+
requests

## Poznámka
Kurzy jsou převzaty z veřejného TXT souboru ČNB:
https://www.cnb.cz/.../denni_kurz.txt
