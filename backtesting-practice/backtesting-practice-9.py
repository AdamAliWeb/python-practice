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

    def next(self):
        if crossover(self.daily_rsi, self.upper_bound):
            if self.position.is_long:
                print(self.position.size)
                print(self.position.pl_pct)
                self.position.close()
                self.sell()

        elif crossover(self.lower_bound, self.daily_rsi):
            if self.position.is_short or not self.position:
                self.position.close()
                self.buy()

bt = Backtest(GOOG, RsiOscillator, cash=10_000, commission=.002)

stats = bt.run()

print(stats)

bt.plot()
