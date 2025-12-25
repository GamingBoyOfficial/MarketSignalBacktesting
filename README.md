# Market Signal Analysis & Backtesting

This project evaluates two trading strategies on NVIDIA (NVDA) using Python:

- **Simple Moving Average (SMA)** crossover strategy
- **MACD momentum strategy**

## Project Overview
The goal is to demonstrate strategy backtesting, performance evaluation, and risk-adjusted analysis using equity curves and the Sharpe ratio.

## What I did
- Collected historical stock data using Yahoo Finance (2020–2025)
- Implemented SMA and MACD strategies in Python
- Backtested strategies with transaction costs using Backtesting.py
- Compared performance using equity curves and **Sharpe ratio** for risk-adjusted returns

## Tools / Libraries
- Python
- Pandas, NumPy
- Backtesting.py
- TA-Lib
- Yahoo Finance

## Key Results
- **SMA Strategy**: Sharpe ratio = 0.53 → moderate risk-adjusted returns  
- **MACD Strategy**: Sharpe ratio = 0.11 → lower risk-adjusted performance  
- Illustrates how different strategies perform under the same market conditions

## Observations
- SMA provided moderate returns with better risk-adjusted performance  
- MACD had low Sharpe ratio due to default parameter mismatch with NVDA trend  
- Strategies are educational and show the process of backtesting, analysis, and risk evaluation  

## Files
- `market_signal_analysis.ipynb` → Full notebook with code, plots, and analysis  
- `backtest.py` → Standalone Python script for running the strategies

## ▶ Run the Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/github/GamingBoyOfficial/MarketSignalBacktesting/blob/main/MarketSignalAnalysis.ipynb)

⚠️ GitHub renders notebooks statically.  
Use Google Colab to execute the code interactively.
