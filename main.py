#!/usr/bin/env python3
"""
BCB Currency Monitor - Find the minimum USD to BRL exchange rate in a month
Uses the official Brazilian Central Bank (BCB) PTAX API
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Tuple, Optional
import sys


class BCBCurrencyMonitor:
    """Monitor and analyze USD to BRL exchange rates from BCB's PTAX API"""
    
    BASE_URL = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'BCB-Currency-Monitor/1.0'
        })
    
    def get_rates_for_period(
        self, 
        start_date: datetime, 
        end_date: datetime
    ) -> list[dict]:
        """
        Fetch exchange rates for a date range from BCB API
        
        Args:
            start_date: Start date (inclusive)
            end_date: End date (inclusive)
            
        Returns:
            List of exchange rate records
        """
        # Format dates as required by API (MM-DD-YYYY)
        data_inicial = start_date.strftime("%m-%d-%Y")
        data_final = end_date.strftime("%m-%d-%Y")
        
        # API endpoint for getting quotations by period
        # The endpoint URL structure must include the date parameters
        endpoint = f"{self.BASE_URL}/CotacaoDolarPeriodo(dataInicial='{data_inicial}',dataFinalCotacao='{data_final}')?$format=json&$orderby=dataHoraCotacao%20asc&$top=500"
        
        try:
            print(f"📡 Fetching exchange rates from {data_inicial} to {data_final}...")
            response = self.session.get(endpoint, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract the value array from the OData response
            rates = data.get("value", [])
            
            if not rates:
                print("⚠️  No data found for the specified period.")
                return []
            
            print(f"✅ Retrieved {len(rates)} exchange rate records")
            return rates
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching data from BCB API: {e}")
            return []
    
    def find_minimum_rate(self, rates: list[dict]) -> Optional[dict]:
        """
        Find the minimum sell rate (best rate for converting USD to BRL)
        
        Args:
            rates: List of exchange rate records
            
        Returns:
            Record with minimum sell rate, or None if no data
        """
        if not rates:
            return None
        
        # Filter for valid rates and find minimum sell rate
        valid_rates = [
            rate for rate in rates 
            if rate.get("cotacaoVenda") is not None
        ]
        
        if not valid_rates:
            return None
        
        minimum = min(valid_rates, key=lambda x: x["cotacaoVenda"])
        return minimum
    
    def find_maximum_rate(self, rates: list[dict]) -> Optional[dict]:
        """
        Find the maximum sell rate (worst rate for converting USD to BRL)
        
        Args:
            rates: List of exchange rate records
            
        Returns:
            Record with maximum sell rate, or None if no data
        """
        if not rates:
            return None
        
        # Filter for valid rates and find maximum sell rate
        valid_rates = [
            rate for rate in rates 
            if rate.get("cotacaoVenda") is not None
        ]
        
        if not valid_rates:
            return None
        
        maximum = max(valid_rates, key=lambda x: x["cotacaoVenda"])
        return maximum
    
    def format_rate_record(self, record: dict) -> str:
        """Format a rate record for display"""
        date = record.get("dataHoraCotacao", "N/A")
        sell_rate = record.get("cotacaoVenda", "N/A")
        buy_rate = record.get("cotacaoCompra", "N/A")
        
        return f"  📅 {date}\n    Sell (USD→BRL): {sell_rate}\n    Buy (BRL→USD): {buy_rate}"
    
    def get_month_rates(self, year: int, month: int) -> Tuple[Optional[dict], Optional[dict]]:
        """
        Get minimum and maximum rates for a specific month
        
        Args:
            year: Year (e.g., 2024)
            month: Month (1-12)
            
        Returns:
            Tuple of (min_rate, max_rate)
        """
        # First day of the month
        start_date = datetime(year, month, 1)
        
        # Last day of the month
        if month == 12:
            end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            end_date = datetime(year, month + 1, 1) - timedelta(days=1)
        
        rates = self.get_rates_for_period(start_date, end_date)
        
        min_rate = self.find_minimum_rate(rates)
        max_rate = self.find_maximum_rate(rates)
        
        return min_rate, max_rate
    
    def display_month_analysis(self, year: int, month: int):
        """Display analysis for a specific month"""
        month_name = datetime(year, month, 1).strftime("%B %Y")
        
        print(f"\n{'='*60}")
        print(f"📊 Exchange Rate Analysis for {month_name}")
        print(f"{'='*60}\n")
        
        min_rate, max_rate = self.get_month_rates(year, month)
        
        if min_rate:
            print("🎯 BEST RATE TO CONVERT USD → BRL (Minimum)")
            print(self.format_rate_record(min_rate))
            print(f"    💵 1 USD = R$ {min_rate['cotacaoVenda']}")
        else:
            print("❌ No minimum rate data available")
        
        print()
        
        if max_rate:
            print("⚠️  WORST RATE TO CONVERT USD → BRL (Maximum)")
            print(self.format_rate_record(max_rate))
            print(f"    💵 1 USD = R$ {max_rate['cotacaoVenda']}")
        else:
            print("❌ No maximum rate data available")
        
        if min_rate and max_rate:
            difference = max_rate['cotacaoVenda'] - min_rate['cotacaoVenda']
            percentage = (difference / min_rate['cotacaoVenda']) * 100
            print(f"\n📈 Difference: R$ {difference:.4f} ({percentage:.2f}%)")
        
        print(f"\n{'='*60}\n")


def main():
    """Main function"""
    monitor = BCBCurrencyMonitor()
    
    # Get current date or use provided date
    if len(sys.argv) > 2:
        try:
            year = int(sys.argv[1])
            month = int(sys.argv[2])
        except ValueError:
            print("Usage: python main.py [year] [month]")
            print("Example: python main.py 2025 12")
            return
    else:
        now = datetime.now()
        year = now.year
        month = now.month
    
    # Validate month
    if not (1 <= month <= 12):
        print(f"❌ Invalid month: {month}. Please use a value between 1 and 12.")
        return
    
    monitor.display_month_analysis(year, month)


if __name__ == "__main__":
    main()
