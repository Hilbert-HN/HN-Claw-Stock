"""
Stock Data Service - Fetch US stock data from Yahoo Finance
"""
import yfinance as yf
import pandas as pd
from typing import List, Dict, Optional
from datetime import datetime


class StockDataService:
    """Service for fetching stock data"""
    
    def __init__(self):
        pass
    
    def get_stock_info(self, symbol: str) -> Optional[Dict]:
        """
        Get basic stock information
        
        Args:
            symbol: Stock symbol (e.g., 'AAPL', 'TSLA')
            
        Returns:
            Dictionary with stock info
        """
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            
            return {
                "symbol": symbol,
                "name": info.get("longName", symbol),
                "price": info.get("currentPrice", info.get("regularMarketPrice")),
                "change": info.get("regularMarketChange"),
                "changePercent": info.get("regularMarketChangePercent"),
                "marketCap": info.get("marketCap"),
                "peRatio": info.get("trailingPE"),
                "dividendYield": info.get("dividendYield"),
                "52WeekHigh": info.get("fiftyTwoWeekHigh"),
                "52WeekLow": info.get("fiftyTwoWeekLow"),
                "volume": info.get("volume"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
            }
        except Exception as e:
            print(f"Error fetching info for {symbol}: {e}")
            return None
    
    def get_historical_data(
        self, 
        symbol: str, 
        period: str = "1mo",
        interval: str = "1d"
    ) -> Optional[pd.DataFrame]:
        """
        Get historical stock price data
        
        Args:
            symbol: Stock symbol
            period: Time period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
            interval: Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
            
        Returns:
            DataFrame with historical data
        """
        try:
            stock = yf.Ticker(symbol)
            df = stock.history(period=period, interval=interval)
            return df
        except Exception as e:
            print(f"Error fetching history for {symbol}: {e}")
            return None
    
    def get_multiple_stocks_info(self, symbols: List[str]) -> List[Dict]:
        """
        Get info for multiple stocks
        
        Args:
            symbols: List of stock symbols
            
        Returns:
            List of stock info dictionaries
        """
        results = []
        for symbol in symbols:
            info = self.get_stock_info(symbol)
            if info:
                results.append(info)
        return results
    
    def search_stocks(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for stocks by keyword
        
        Args:
            query: Search query
            limit: Maximum number of results
            
        Returns:
            List of matching stocks
        """
        # yfinance doesn't have built-in search, would need alternative API
        # For now, return empty list
        return []


# Singleton instance
stock_service = StockDataService()
