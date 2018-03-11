import random
import unittest
from TradeData import TradeData
from StockCalculations import StockCalculations

class FunctionalTest(unittest.TestCase):

    stocks = {'1': "TEA", '2': "POP", '3': "ALE", '4': "GIN", '5': "JOE"}
    symbols =['1','2','3','4','5']

    types = [1, 2]
    quantities = range(0, 100, 2)
    prices = [123,435,5756,34645,3534,756]


    def test_recordTradeTest(self):
        print('\ntest_recordTradeTest\n')
        for i in range(5):
            StockCalculations().tradeRecord(random.choice(self.symbols), random.choice(self.quantities), random.choice(self.types),
                                 random.choice(self.prices))


    def test_stockPriceTest(self):
        print('\ntest_stockPriceTest\n')
        for symbol in self.symbols:
            print('Stock price for %s:' % self.stocks[symbol],StockCalculations().volumeWeightedStockPrice(symbol))


    def test_dividendCalcTest(self):
        print('\ntest_dividendCalcTest\n')
        for symbol in self.symbols:
             print 'Dividend for %s:' % self.stocks[symbol],StockCalculations().dividendCalc(symbol, float(random.choice(self.prices)))


    def test_peratioTest(self):
        print('\ntest_peratioTest\n')
        for symbol in self.symbols:
            print 'P/E Ratio for %s:' % self.stocks[symbol],StockCalculations().peRatioCalc(symbol, float(random.choice(self.prices)))


    def test_shareIndexTest(self):
        print('\ntest_shareIndexTest\n')



if __name__ == '__main__':
    unittest.main()
