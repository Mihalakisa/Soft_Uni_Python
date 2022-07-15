import yfinance as f
import easygui

company = f.Ticker('TSLA')
stock_data = company.history(period='1mo')

# easygui.msgbox(f'{company.info}', title='simple qui')
easygui.msgbox(f'{stock_data}', title='simple qui')