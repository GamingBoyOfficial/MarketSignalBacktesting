"""
Market Signal Analysis & Backtesting
Author: Parikshit

Compares SMA and MACD trading strategies on NVDA.
Originally prototyped in Google Colab.
"""

import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yk
import pandas as pd
import numpy as np
import talib

from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA


class SMAStrategy(Strategy):
    def init(self):
        price = self.data.Close
        self.m10 = self.I(SMA, price, 10)
        self.m20 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.m10, self.m20):
            self.buy()
        elif crossover(self.m20, self.m10):
            self.sell()


class MACDStrategy(Strategy):
    def init(self):
        price = self.data.Close
        self.macd = self.I(lambda x: talib.MACD(x)[0], price)
        self.macd_signal = self.I(lambda x: talib.MACD(x)[1], price)

    def next(self):
        if crossover(self.macd, self.macd_signal):
            self.buy()
        elif crossover(self.macd_signal, self.macd):
            self.sell()


def sharpe_ratio(equity_curve):
    returns = equity_curve.pct_change().dropna()
    sharpe = (returns.mean() / returns.std()) * np.sqrt(252)
    return round(sharpe, 2)


if __name__ == "__main__":
    stock = "NVDA"
    begin = dt.datetime(2020, 1, 1)
    finish = dt.datetime(2025, 1, 1)

    data = yk.download(stock, start=begin, end=finish)
    data.columns = data.columns.get_level_values(0)

    sma_bt = Backtest(data, SMAStrategy, commission=0.002, exclusive_orders=True)
    macd_bt = Backtest(data, MACDStrategy, commission=0.002, exclusive_orders=True)

    sma_stats = sma_bt.run()
    macd_stats = macd_bt.run()

    print("SMA Strategy Results")
    print(sma_stats)

    print("\nMACD Strategy Results")
    print(macd_stats)

    sma_curve = sma_stats._equity_curve['Equity']
    macd_curve = macd_stats._equity_curve['Equity']

    print("\nSMA Sharpe Ratio:", sharpe_ratio(sma_curve))
    print("MACD Sharpe Ratio:", sharpe_ratio(macd_curve))

    plt.figure(figsize=(12, 6))
    plt.plot(sma_curve, label="SMA Strategy")
    plt.plot(macd_curve, label="MACD Strategy")
    plt.legend()
    plt.title("SMA vs MACD Equity Curve Comparison (NVDA)")
    plt.show()
