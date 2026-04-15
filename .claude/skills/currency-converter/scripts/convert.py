import urllib.request
import json
import sys


def convert(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(json.dumps({"error": f"Could not fetch rates: {e}"}))
        sys.exit(1)

    if data.get("result") != "success":
        print(json.dumps({"error": f"API error: {data.get('error-type', 'unknown')}"}))
        sys.exit(1)

    rates = data.get("rates", {})
    if to_currency not in rates:
        print(json.dumps({"error": f"Unsupported currency: {to_currency}"}))
        sys.exit(1)

    rate = rates[to_currency]
    converted = round(amount * rate, 2)

    print(json.dumps({
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "converted": converted,
        "rate": rate
    }))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(json.dumps({"error": "Usage: convert.py <amount> <from> <to>"}))
        sys.exit(1)

    try:
        amount = float(sys.argv[1])
    except ValueError:
        print(json.dumps({"error": f"Invalid amount: {sys.argv[1]}"}))
        sys.exit(1)

    convert(amount, sys.argv[2], sys.argv[3])
