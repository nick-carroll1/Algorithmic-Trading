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
        self.PricesInitialized = False
        self.GOOGStartPrice = 0
        self.AMZNStartPrice = 0
        self.holdingGOOG = False
        self.holdingAMZN = False

    def OnData(self, data: Slice):
        if self.PricesInitialized == False:
            self.GOOGStartPrice = self.Portfolio['GOOG'].Price
            self.AMZNStartPrice = self.Portfolio['AMZN'].Price
            self.PricesInitialized = True
        if (self.holdingGOOG == False) and (self.Portfolio['GOOG'].Price < self.GOOGStartPrice * .95):
            self.MarketOrder("GOOG", 6_000)
            self.holdingGOOG = True
        if (self.holdingAMZN == False) and (self.Portfolio['AMZN'].Price > self.AMZNStartPrice * 1.05):
            self.MarketOrder("AMZN", -8_000)
            self.holdingAMZN = True 