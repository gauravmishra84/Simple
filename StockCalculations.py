from datetime import datetime, timedelta
import csv,pickle,os
from pprint import pprint as pp
import TradeData

#Reading the CSV file 

csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

tradeData = list(csv.DictReader('data.csv', dialect='piper'))

symbols = ['TEA', 'POP', 'ALE', 'GIN', 'JOE']
stocks = dict(enumerate(symbols, 1))

indicators = ['BUY', 'SELL']
indicatorMap = dict(enumerate(indicators, 1))

class StockCalculations():
    '''
    This class is containing all the trade scenario calculations mentioned in the assignment
    '''


    def dividendCalc(self,Symbol,Price):
        '''
        Calculation of divident yeild. 
        :param stockSymbol: stock symbol
        :param stockPrice: input price for the stock
        :return: dividend
        '''
        
        stockSymbol= stocks.get(int(Symbol),None)
        print (stockSymbol)
        
        if stockSymbol is None:
                return False
            

        if float(Price) == 0.00 :
                return False
                raise ZeroDivisionError
        
        for stck in tradeData:
            if stck['stockSymbol'] == stockSymbol:
                if stck['stockType'] == 'Common':
                    dividend = float(stck.get(lastDividend,0))/float(Price)
                elif stck['stockType'] == 'Preferred':
                    dividend = (float(stck.get(fixedDividend,0))/100) * (float(stck.get(parValue,0))/ float(Price))
                else:
                    pass
        return dividend

    
    def peRatioCalc(self,stockSymbol,stockPrice):
        '''
        Calculation of P E ratio
        :param stockSymbol:
        :param stockPrice:
        :return: PE ration
        '''
        dividend= self.dividendCalc(stockSymbol,stockPrice)
        peratio = float(stockPrice)/float(dividend)
        return peratio


    def deletefileContent(fileName):
        f= open('fileName',w)
        f.close()

    def tradeRecord(self,stockSymbol, stockQuantity, indicator, stockTradePrice):
        '''
        Recording the trade in the file
        :param stockSymbol:
        :param stockQuantity:
        :param indicator:
        :param stockTradePrice:
        :return: record the trade in the tradeRecord file
        '''
        tradeRecordFile = open('tradeRecord','r')
        if not os.path.getsize("tradeRecord") == 0:
            listRecord = pickle.load(tradeRecordFile)
        else:
            listRecord = []


        stockSymbol=stocks.get(None)
        stockQuantity= int(stockQuantity)
        indicator=indicatorMap.get(None)
        stockTradePrice=float(stockTradePrice)

        try:
            recordData=TradeData(stockSymbol,stockQuantity,indicator,stockTradePrice,datetime.now())
            tradeRecordFile=open('tradeRecord','w')
            listRecord.append(recordData)
            pickle.dump(listRecord,tradeRecordFile)
            pp('Trade Record : ',recordData.tradeDetails())
        except EOFError:
            pp('No print Data')
        
        tradeRecordFile.close()


    def volumeWeightedStockPrice(self,stockSymbol):

        '''
        Calculation of voumne weighted stock price in last 5 mins
        :param stockSymbol:
        :return:
        '''
        stockSymbol=stocks.get(None)
        tradeTime = datetime.now()-timedelta(minutes=5)
        totalQuantity = 0
        priceSum=0


        tradeRecordFile= open('tradeRecord','r')
        if not os.path.getsize('tradeRecord')==0:
            listRecord = pickle.load(tradeRecordFile)
            for r in listRecord:
                if r.stockSymbol == stockSymbol and r.tradeCreationTime >= tradeTime:
                    r.tradeDetails()
                    totalQuantity = r.stockQuantity
                    priceSum== (r.stockQuantity *r.stockTradePrice)

            if priceSum >0 and totalQuantity >0 :
                volumeWeightedStockPrice = priceSum/totalQuantity
                print ('Volumen Weighted Stock Price: ',float(volumeWeightedStockPrice))
            else:
                print ('No trade record for the given stock {} in last 5 mins'.format(stockSymbol))


    def shareIndex(self):

        '''
        Share index calculation
        :return: prints the share index
        '''
        priceSum= 0
        totalQuantity= 0
        tradeRecordFile= open('tradeRecord','r')
        
        if not os.path.getsize('tradeRecord')==0:
            listRecord= pickle.load(tradeRecordFile)
            
            for r in listRecord:
                if r.stockSymbol == stockSymbol and r.tradeCreationTime >= tradeTime:
                    r.tradeDetails()
                    totalQuantity = r.stockQuantity
                    priceSum== (r.stockQuantity * r.stockTradePrice)

            if priceSum > 0 and totalQuantity > 0:
                gbceShareIndex = priceSum ** (1/totalQuantity)

                print('Share Index: ', gbceShareIndex)
            else:
                return 'No trade records'
















