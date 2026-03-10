"""
Stock Data Service - Fetch US stock data (Simple version for Python 3.6)
"""
import requests
from typing import List, Dict, Optional
from datetime import datetime


class StockDataService:
    """Service for fetching stock data"""
    
    def __init__(self):
        self.base_url = "https://query1.finance.yahoo.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    
    def get_stock_info(self, symbol: str) -> Optional[Dict]:
        """
        Get basic stock information (mock data for demo)
        
        In production, this would fetch from Yahoo Finance API
        """
        # Mock data for demo purposes
        # In production, use: https://query1.finance.yahoo.com/v8/finance/chart/{symbol}
        
        mock_stocks = {
            "AAPL": {"name": "Apple Inc.", "price": 175.50, "change": 2.30, "changePercent": 1.33},
            "MSFT": {"name": "Microsoft Corporation", "price": 415.20, "change": -1.50, "changePercent": -0.36},
            "GOOGL": {"name": "Alphabet Inc.", "price": 140.80, "change": 0.90, "changePercent": 0.64},
            "AMZN": {"name": "Amazon.com Inc.", "price": 178.30, "change": 3.20, "changePercent": 1.83},
            "TSLA": {"name": "Tesla Inc.", "price": 248.50, "change": -5.40, "changePercent": -2.13},
            "NVDA": {"name": "NVIDIA Corporation", "price": 875.30, "change": 12.50, "changePercent": 1.45},
            "META": {"name": "Meta Platforms Inc.", "price": 485.60, "change": 4.20, "changePercent": 0.87},
            "NFLX": {"name": "Netflix Inc.", "price": 598.40, "change": -2.80, "changePercent": -0.47},
        }
        
        if symbol.upper() in mock_stocks:
            data = mock_stocks[symbol.upper()]
            return {
                "symbol": symbol.upper(),
                "name": data["name"],
                "price": data["price"],
                "change": data["change"],
                "changePercent": data["changePercent"],
                "marketCap": None,
                "peRatio": None,
                "volume": None,
                "sector": "Technology",
                "rsi": 50,  # Placeholder
            }
        
        # Return generic data for unknown stocks
        return {
            "symbol": symbol.upper(),
            "name": symbol.upper() + " Inc.",
            "price": 100.00,
            "change": 0.00,
            "changePercent": 0.00,
            "marketCap": None,
            "peRatio": None,
            "volume": None,
            "sector": "Unknown",
            "rsi": 50,
        }
    
    def get_historical_data(self, symbol: str, period: str = "1mo", interval: str = "1d"):
        """Get historical data (placeholder)"""
        return None
    
    def get_multiple_stocks_info(self, symbols: List[str]) -> List[Dict]:
        """Get info for multiple stocks"""
        results = []
        for symbol in symbols:
            info = self.get_stock_info(symbol)
            if info:
                results.append(info)
        return results


# Singleton instance
stock_service = StockDataService()
