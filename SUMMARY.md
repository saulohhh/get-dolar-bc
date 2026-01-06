# 📊 BCB Currency Monitor - Project Summary

## What Was Created

A complete Python application that monitors USD to BRL (US Dollar to Brazilian Real) exchange rates using the **official Brazilian Central Bank (BCB) API**.

### Key Features

✅ **Official Data Source**: Uses BCB's PTAX API (dadosabertos.bcb.gov.br)
✅ **Find Best Rates**: Identifies the lowest exchange rate for USD→BRL conversion in any month
✅ **Compare Rates**: Shows both best and worst rates plus the difference
✅ **Interactive CLI**: User-friendly interactive mode or command-line arguments
✅ **Historical Data**: Access rates from November 1984 to present
✅ **Real-time Updates**: Pulls current data directly from BCB's API

## Project Structure

```
bcb_currency_monitor/
├── main.py              # Core application logic
├── cli.py              # Interactive CLI interface
├── requirements.txt    # Python dependencies
├── README.md          # User documentation
└── SUMMARY.md         # This file
```

## How to Use

### Option 1: Interactive Mode (Recommended)
```bash
python3 cli.py
```
Provides a friendly prompt to enter month and year.

### Option 2: Command Line
```bash
# Current month
python3 main.py

# Specific month
python3 main.py 2025 12
```

## Sample Output

```
============================================================
📊 Exchange Rate Analysis for January 2025
============================================================

🎯 BEST RATE TO CONVERT USD → BRL (Minimum)
  📅 2025-01-31 13:03:54.994
    Sell (USD→BRL): 5.8301
    Buy (BRL→USD): 5.8295
    💵 1 USD = R$ 5.8301

⚠️  WORST RATE TO CONVERT USD → BRL (Maximum)
  📅 2025-01-02 13:09:42.489
    Sell (USD→BRL): 6.2086
    Buy (BRL→USD): 6.208
    💵 1 USD = R$ 6.2086

📈 Difference: R$ 0.3785 (6.49%)

============================================================
```

## Technical Details

### Technology Stack
- **Language**: Python 3.9+
- **HTTP Client**: `requests` library
- **API**: BCB PTAX API (OData protocol)
- **Data Format**: JSON

### API Endpoint
```
https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata
```

### Supported Methods
- `CotacaoDolarPeriodo` - Get exchange rates for a date range
- Filters by date range and returns buy/sell quotations

### Data Available
- **Sell Rate** (`cotacaoVenda`): Rate for converting USD → BRL
- **Buy Rate** (`cotacaoCompra`): Rate for converting BRL → USD
- **Date/Time**: Exact timestamp of the quotation
- **Multiple Bulletins**: Opening, intermediate, and closing rates

## Installation

1. Clone or navigate to the project:
```bash
cd bcb_currency_monitor
```

2. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

3. Run the application:
```bash
python3 cli.py
```

## Use Cases

🏦 **Currency Traders**: Track the best time to convert currencies
💼 **Business People**: Monitor exchange rates for international transactions
📈 **Investors**: Analyze historical exchange rate trends
🌍 **Travelers**: Find the best rates for currency exchange

## License

This project uses open data from the Brazilian Central Bank (BCB) under the Open Data Commons Open Database License (ODbL).

## Additional Resources

- Official API: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/documentacao
- Open Data Portal: https://dadosabertos.bcb.gov.br/
- BCB Website: https://www.bcb.gov.br/

---

**Created**: January 2026
**Version**: 1.0
