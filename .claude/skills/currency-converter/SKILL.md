---
name: currency-converter
description: This skill should be used when the user asks to "convert currency", "check exchange rates", "convert MNT", "convert tugrik", asks "how much is X in dollars", "how much is X in tugrik", or mentions any currency conversion involving Mongolian Tugrik (MNT), USD, EUR, KRW, CNY, or JPY.
version: 0.1.0
---

# MNT Currency Converter

Convert between Mongolian Tugrik (MNT) and major currencies using live exchange rates.

## Supported Currencies

- MNT — Mongolian Tugrik
- USD — US Dollar
- EUR — Euro
- KRW — South Korean Won
- CNY — Chinese Yuan
- JPY — Japanese Yen

## How to Convert

Run the conversion script:

```bash
python3 .claude/skills/currency-converter/scripts/convert.py <amount> <from_currency> <to_currency>
```

The script outputs JSON with the converted amount and exchange rate.

If only an amount and one currency are given, default the other currency to MNT. For example, "how much is 100 USD" means convert 100 USD to MNT.

## Output Format

Present the result conversationally:
- Show the converted amount rounded to 2 decimal places
- Show the exchange rate used
- For small MNT amounts (under 50,000 MNT), add a fun note like "That's about the price of X khuushuur" (one khuushuur costs roughly 3,000-5,000 MNT)
- Keep responses short and friendly

## Error Handling

If the script returns an error (network failure, unsupported currency), tell the user live rates are unavailable and suggest trying again. Never guess exchange rates.
