import yfinance as yf
import pandas as pd
from typing import Optional

class DilutionDetector:
    def __init__(self, ticker_symbol: str):
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)
        
        # data structures that will hold the final output
        self.shares_data: Optional[pd.DataFrame] = None 
        self.yearly_dilution_pct: Optional[pd.Series] = None
        self.alerts: list = []

    def fetch_and_normalize_shares(self) -> bool:
        try:
            # 1. Fetch historical outstanding shares
            raw_shares = self.ticker.get_shares_full(start="1990-01-01", end=None)
            
            if raw_shares is None or raw_shares.empty:
                print(f"No shares data found for {self.ticker_symbol}.")
                return False

            # 2. Fetch split history
            splits = self.ticker.splits

            # 3  Create the main DataFrame and standardize time indices to UTC
            df = pd.DataFrame(raw_shares, columns=['Raw_Shares'])
            df.index = pd.to_datetime(df.index, utc=True).normalize()
            
            df['Split_Multiplier'] = 1.0

            # 4. Normalization Logic
            if not splits.empty:
                splits.index = pd.to_datetime(splits.index, utc=True).normalize()
                
                for split_date, split_factor in splits.items():
                    # Apply the multiplier to all dates prior to the split
                    mask_before_split = df.index < split_date
                    df.loc[mask_before_split, 'Split_Multiplier'] *= split_factor
                    
                    # Catch Reverse Splits (Severe Alert)
                    if split_factor < 1.0:
                        self.alerts.append(
                            f"🚨 REVERSE SPLIT detected on {split_date.strftime('%Y-%m-%d')} (Factor: {split_factor})"
                        )

            # 5. Calculate the Adjusted Shares (Real Shares)
            df['Adjusted_Shares'] = df['Raw_Shares'] * df['Split_Multiplier']
            self.shares_data = df
            return True

        except Exception as e:
            print(f"Error processing {self.ticker_symbol}: {e}")
            return False

    def calculate_dilution_metrics(self) -> bool:
        if self.shares_data is None or self.shares_data.empty:
            print("No normalized data available. Run fetch first.")
            return False
            
        # Extract year-end data and calculate YoY percentage
        yearly_data = self.shares_data['Adjusted_Shares'].resample('YE').last()
        self.yearly_dilution_pct = yearly_data.pct_change() * 100
        
        # Alert logic
        for date, pct in self.yearly_dilution_pct.dropna().items():
            year_str = date.strftime('%Y')
            
            if pct > 10.0:
                self.alerts.append(f"🚩 {year_str}: SEVERE Dilution (+{pct:.2f}%)")
            elif pct > 5.0:
                self.alerts.append(f"⚠️ {year_str}: Significant Dilution (+{pct:.2f}%)")
            elif pct > 0.0:
                self.alerts.append(f"⚪ {year_str}: Stable / Minor Dilution (+{pct:.2f}%)")
            else:
                self.alerts.append(f"🟢 {year_str}: Positive / Stock Buyback ({pct:.2f}%)")
                
        return True