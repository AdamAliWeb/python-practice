from backtesting import Backtest, Strategy
from backtesting.test import GOOG

from backtesting.lib import crossover

import talib

# print(GOOG.head(10))

# ToDo: 1) Set Week Avg. 2) Set Take Profit and Stop Loss 3) Set closing condition (set to none week values)

class PeriodBreakingStrategy(Strategy):
    week_max = None
    week_min = None
    stop_loss = None
    take_profit = None

    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, 14)

    def next(self):
        if (self.data.index[-1].isocalendar()[2] == 1):
            self.week_max = self.data.High[-6:-1].max()
            self.week_min = self.data.Low[-6:-1].min()

        if (self.week_max is not None and self.week_min is not None) and self.data.Close[-1] > self.week_max and not self.position:
            self.stop_loss = (self.week_max - self.week_min) / 2 + self.week_min
            self.take_profit = self.data.Close[-1] + (self.week_max - self.week_min)

            self.position.close()
            self.buy(sl=self.stop_loss, tp=self.take_profit)
        # elif (self.week_max is not None and self.week_min is not None) and self.data.Close[-1] < self.week_min and not self.position:
        #     self.stop_loss = (self.week_max - self.week_min) / 2 + self.week_min
        #     self.take_profit = self.data.Close[-1] - (self.week_max - self.week_min)

        #     self.position.close()
        #     self.sell(sl=self.stop_loss, tp=self.take_profit)

bt = Backtest(GOOG, PeriodBreakingStrategy, cash=10_000, commission=.002)

stats = bt.run()
print(stats)
bt.plot()