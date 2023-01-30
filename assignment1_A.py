# region imports
from AlgorithmImports import *
# endregion

class CreativeFluorescentPinkTermite(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 1, 1)
        self.SetCash(1_000_000)  # Set Strategy Cash
        self.AddEquity("GOOG", Resolution.Daily)
        self.AddEquity("AMZN", Resolution.Daily)
        self.holding = False

    def OnData(self, data: Slice):
        if self.holding == False:
            self.MarketOrder("GOOG", 6_000)
            self.MarketOrder("AMZN", -8_000)
            self.holding = True
        elif self.Portfolio.TotalPortfolioValue < 900_000:
            self.MarketOrder("GOOG", -6_000)
            self.MarketOrder("AMZN", 8_000)