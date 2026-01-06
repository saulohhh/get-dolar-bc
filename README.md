# BCB Currency Monitor

A Python application that accesses the Brazilian Central Bank (Banco Central do Brasil) official exchange rate data to find the **minimum USD to BRL conversion rate** in a given month.

## Features

- 🔗 Uses official BCB PTAX API (dadosabertos.bcb.gov.br)
- 📊 Analyzes daily exchange rates for any month
- 🎯 Finds the best rate to convert USD → BRL (minimum value)
- ⚠️ Shows the worst rate (maximum value) for comparison
- 📈 Calculates the difference and percentage variation
- 🔄 Works with historical data since November 1984

## Prerequisites

- Python 3.9+
- `requests` library

## Installation

```bash
# Clone or navigate to the project directory
cd bcb_currency_monitor

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Interactive Mode (Recommended)
```bash
python3 cli.py
```
This opens an interactive prompt where you can enter the month and year you want to check.

### Command Line Mode

Get rates for the current month:
```bash
python3 main.py
```

Get rates for a specific month:
```bash
python3 main.py 2025 12
```

Get rates for a different month:
```bash
python3 main.py 2024 6
```

### Usage Notes
- Months should be provided as numbers (1-12)
- Years can be from 1984 onwards
- Exchange rates are only available for business days
- If you query a non-business day, you'll get the rate from the previous business day

## Output Example

```
============================================================
📊 Exchange Rate Analysis for December 2025
============================================================

🎯 BEST RATE TO CONVERT USD → BRL (Minimum)
  📅 12-10-2025
    Sell (USD→BRL): 5.1234
    Buy (BRL→USD): 0.1952
    💵 1 USD = R$ 5.1234

⚠️  WORST RATE TO CONVERT USD → BRL (Maximum)
  📅 12-02-2025
    Sell (USD→BRL): 5.3456
    Buy (BRL→USD): 0.1871
    💵 1 USD = R$ 5.3456

📈 Difference: R$ 0.2222 (4.33%)

============================================================
```

## API Reference

The app uses the official BCB PTAX API:
- **Endpoint**: `https://olinda.bcb.gov.br/olinda/servico/PTAX/`
- **Documentation**: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/documentacao
- **Data Portal**: https://dadosabertos.bcb.gov.br/

## Notes

- Exchange rates are updated daily by the BCB
- The API provides rates for business days (useful days)
- Rates are in the format: 1 USD = X BRL (sell rate)
- Data available from November 28, 1984 onwards

## License

This project uses open data from the Brazilian Central Bank (BCB) under the Open Data Commons Open Database License (ODbL).

