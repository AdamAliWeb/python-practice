from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover, plot_heatmaps, resample_apply

import matplotlib.pyplot as plt
import seaborn as sns
import talib

# print(GOOG.head(10))

def optim_func(series):
    if series["# Trades"] < 10:
        return -1
    
    return series["Equity Final [$]"] / series["Exposure Time [%]"]

class RsiOscillator(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    def init(self):
        self.daily_rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)
        self.weekly_rsi = resample_apply(
            "W-FRI", talib.RSI, self.data.Close, self.rsi_window
        )

    def next(self):
        if crossover(self.daily_rsi, self.upper_bound) and self.weekly_rsi[-1] > self.upper_bound:
            self.position.close()
        elif crossover(self.lower_bound, self.daily_rsi) and self.weekly_rsi[-1] < self.lower_bound:
            self.buy()

bt = Backtest(GOOG, RsiOscillator, cash=10_000, commission=.002)

stats = bt.run()

print(stats)

bt.plot()
