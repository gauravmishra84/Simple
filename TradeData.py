class TradeData():
    '''
    This class is for recording the trading systems data.
    '''


    def __init__(self,stockSymbol, stockQuantity, indicator, stockTradePrice, tradeCreationTime):
        self.stockSymbol = stockSymbol
        self.stockQuantity = stockQuantity
        self.indicator = indicator
        self.stockTradePrice= stockTradePrice
        self.tradeCreationTime = tradeCreationTime

    def tradeDetails(self):
        tradeData = "stockSymbol : {0} \n stockQuantity : {1} \n Indicator : {2} \n stockTradePrice : {3} \n tradeCreationTime : {4}".format(
            self.stockSymbol, self.stockQuantity, self.indicator, self.stockTradePrice, self.tradeCreationTime)
        return tradeData