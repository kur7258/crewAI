import yfinance as yf
from crewai_tools import tool, ScrapeWebsiteTool

# Agents의 stock news 검색을 위한 도구
@tool("Stock News")
def stock_news(ticker):
    '''
        Useful to get news about a stock.
        The input should be a ticker, for example AAPL, NET.
    '''
    ticker = yf.Ticker(ticker)
    return ticker.news

# Agents의 website 검색을 위한 도구
scrape_tool = ScrapeWebsiteTool()

# Agents의 주가 추이 확인을 위한 도구
@tool('Stock Price')
def stock_price(ticker):
    '''
        Useful to get stock price data.
        The input should be a ticker, for example AAPL, NET.
    '''
    ticker = yf.Ticker(ticker)
    return ticker.history(period='1mo')

# Agents의 회사 소득 명세서 확인을 위한 도구
@tool('Income Statement')
def income_stmt(ticker):
    '''
        Useful to get the income statement of a company.
        The input to this tool should be a ticker, for example AAPL, NET.
    '''
    ticker = yf.Ticker(ticker)
    return ticker.income_stmt

# Agents의 회사 대차 대조표 확인을 위한 도구
@tool('Balance Sheet')
def balance_sheet(ticker):
    '''
        Useful to get the balance sheet of a company.
        The input to this tool should be a ticker , for example AAPL, NET.
    '''
    ticker = yf.Ticker(ticker)
    return ticker.balance_sheet

# Agents의 회사 내부자 거래 내역 확인을 위한 도구
@tool('Insider Transactions')
def insider_transactions(ticker):
    '''
        Useful to get the insider transactions of a stock.
        The input to this tool should be a ticker, for example AAPL, NET.
    '''
    ticker = yf.Ticker(ticker)
    return ticker.insider_transactions