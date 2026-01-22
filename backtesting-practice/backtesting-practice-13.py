from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover, plot_heatmaps, resample_apply, barssince

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
    position_size = 1


    def init(self):
        self.daily_rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)

    def next(self): 
        if (self.daily_rsi[-1] > self.upper_bound and barssince(self.daily_rsi < self.upper_bound) == 3):
            self.position.close()
          
        elif self.lower_bound > self.daily_rsi[-1]:
            self.buy(size=self.position_size)

bt = Backtest(GOOG, RsiOscillator, cash=10_000, commission=.002)

stats = bt.run()

print(stats)

bt.plot()
