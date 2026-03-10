"""
Stock API Endpoints
"""
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.services.stock_service import stock_service
from app.services.ai_service import ai_service

router = APIRouter(prefix="/api/stocks", tags=["stocks"])


@router.get("/{symbol}")
async def get_stock_info(symbol: str):
    """
    Get stock information and AI analysis
    
    Args:
        symbol: Stock symbol (e.g., AAPL, TSLA)
        
    Returns:
        Stock info with AI recommendation
    """
    # Get stock data
    stock_info = stock_service.get_stock_info(symbol.upper())
    
    if not stock_info:
        raise HTTPException(status_code=404, detail=f"Stock {symbol} not found")
    
    # Get historical data for analysis
    hist_data = stock_service.get_historical_data(symbol.upper(), period="3mo")
    
    # Calculate simple metrics (placeholder for technical indicators)
    if hist_data is not None and len(hist_data) > 0:
        # Simple RSI calculation (placeholder)
        stock_info["rsi"] = 50  # TODO: Calculate real RSI
    else:
        stock_info["rsi"] = 50
    
    # Get AI analysis
    analysis = ai_service.analyze_stock(stock_info)
    
    return {
        "stock": stock_info,
        "analysis": analysis,
    }


@router.get("/screener")
async def screen_stocks(
    sector: Optional[str] = Query(None, description="Filter by sector"),
    min_market_cap: Optional[float] = Query(None, description="Minimum market cap"),
    max_pe: Optional[float] = Query(None, description="Maximum P/E ratio"),
    limit: int = Query(20, description="Number of results"),
):
    """
    Screen stocks based on criteria
    
    Returns:
        List of stocks matching criteria
    """
    # TODO: Implement proper stock screener
    # For now, return sample stocks
    
    sample_stocks = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "NFLX"]
    
    results = []
    for symbol in sample_stocks[:limit]:
        info = stock_service.get_stock_info(symbol)
        if info:
            analysis = ai_service.analyze_stock(info)
            results.append({
                "stock": info,
                "analysis": analysis,
            })
    
    return {
        "count": len(results),
        "stocks": results,
    }


@router.post("/{symbol}/analyze")
async def analyze_stock(symbol: str):
    """
    Get fresh AI analysis for a stock
    
    Returns:
        AI analysis result
    """
    stock_info = stock_service.get_stock_info(symbol.upper())
    
    if not stock_info:
        raise HTTPException(status_code=404, detail=f"Stock {symbol} not found")
    
    analysis = ai_service.analyze_stock(stock_info)
    
    return analysis
