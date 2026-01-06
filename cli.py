#!/usr/bin/env python3
"""
Interactive CLI for BCB Currency Monitor
Allows users to easily check exchange rates without command line arguments
"""

import sys
from datetime import datetime
from main import BCBCurrencyMonitor


def print_welcome():
    """Print welcome message"""
    print("\n" + "="*60)
    print("🇧🇷 BCB Currency Monitor - USD to BRL Exchange Rates")
    print("="*60 + "\n")


def get_month_input() -> tuple:
    """Get month and year from user input"""
    while True:
        try:
            month = input("Enter month (1-12) [current month]: ").strip()
            year = input("Enter year (e.g., 2025) [current year]: ").strip()
            
            if not month:
                now = datetime.now()
                month = now.month
            else:
                month = int(month)
                if not (1 <= month <= 12):
                    print("❌ Invalid month. Please enter a value between 1 and 12.\n")
                    continue
            
            if not year:
                now = datetime.now()
                year = now.year
            else:
                year = int(year)
                if year < 1984 or year > 2100:
                    print("❌ Invalid year. Data is available from 1984 onwards.\n")
                    continue
            
            return year, month
        except ValueError:
            print("❌ Please enter valid numbers.\n")


def main():
    """Main CLI function"""
    print_welcome()
    
    monitor = BCBCurrencyMonitor()
    
    while True:
        year, month = get_month_input()
        
        print()
        monitor.display_month_analysis(year, month)
        
        again = input("Check another month? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Thank you for using BCB Currency Monitor!\n")
            break


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If arguments provided, use the original non-interactive mode
        from main import main as original_main
        original_main()
    else:
        main()
