from backtesting import Backtest, Strategy
from backtesting.test import GOOG

from backtesting.lib import crossover

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
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()

bt = Backtest(GOOG, RsiOscillator, cash=10_000, commission=.002)


stats = bt.optimize(
    upper_bound=range(55, 85, 1),
    lower_bound=range(10, 45, 1),
    rsi_window=range(10, 30, 1),
    maximize=optim_func,
    constraint= lambda param: param.upper_bound > param.lower_bound,
    max_tries=100 # Tries random numbers in the upper/lower/window ranges
)

print(stats)

# upper_bound = stats["_strategy"].upper_bound
# bt.plot(filename=f"plots/plot-{upper_bound}.html")

bt.plot()