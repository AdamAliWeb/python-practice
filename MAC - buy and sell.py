from backtesting import Backtest, Strategy
from backtesting.test import GOOG

from backtesting.lib import crossover

import talib

# print(GOOG.head(10))

class MovingAverageCrossover(Strategy):
    def init(self):
        self.sma_fast = self.I(talib.SMA, self.data.Close, 5)
        self.sma_slow = self.I(talib.SMA, self.data.Close, 10)
        self.stochastic = self.I(talib.STOCH, self.data.High, self.data.Low, self.data.Close,
                                   fastk_period=14, slowk_period=3, slowd_period=3)

    def next(self):
        if (crossover(self.sma_fast, self.sma_slow) and self.stochastic[-1] > self.stochastic[-2] and self.stochastic[-1] < 80):
            print(f"El supuesto mayor: {self.stochastic[-1]}", f"El supuesto menor: {self.stochastic[-2]}")
            self.position.close()
            self.buy()
        elif (crossover(self.sma_slow, self.sma_fast) and self.stochastic[-1] < self.stochastic[-2] and self.stochastic[-1] > 20):
            self.position.close()
            self.sell()

bt = Backtest(GOOG, MovingAverageCrossover, cash=10_000, commission=.002)
stats = bt.run()
# print(stats)
bt.plot()