from __future__ import division
from datetime import datetime, timedelta
import csv,os
from pprint import pprint as pp
from TradeData import TradeData




#Reading the CSV file 

csv.register_dialect('piper', delimiter=',', quoting=csv.QUOTE_NONE)
reader= csv.reader(open('data.csv'))
filedata=[]
for line in reader:
    filedata.append(line)




symbols = { '1': "TEA",    '2': "POP",    '3': "ALE",    '4': "GIN",    '5': "JOE"}

indicatorMap = { '1': "BUY",    '2': "SELL"}



class StockCalculations():
    '''
    This class is containing all the trade scenario calculations mentioned in the assignment
    '''



    def dividendCalc(self,symbol,price):
        '''
        Calculation of divident yeild. 
        :param stockSymbol: stock symbol
        :param stockPrice: input price for the stock
        :return: dividend
        '''

        stockSymbol= symbols.get(symbol)

        if stockSymbol is None or float(price) == 0.0:
                return False

        if filedata[int(symbol)][0] == str(stockSymbol):
            if filedata[int(symbol)][1] == 'Common':
                dividend = float(filedata[int(symbol)][2])/float(price)
            elif filedata[int(symbol)][1] == 'Preferred':
                dividend = (float(filedata[int(symbol)][3])/100) * (float(filedata[int(symbol)][4])/ float(price))
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
        peratio = 0
        try:
            dividend= self.dividendCalc(stockSymbol,stockPrice)
            peratio = float(stockPrice)/float(dividend)
        except ZeroDivisionError:
            pass
        return peratio


    def tradeRecord(self,Symbol, Quantity, ind,tradePrice):
        '''
        Recording the trade in the file
        :param stockSymbol:
        :param stockQuantity:
        :param indicator:
        :param stockTradePrice:
        :return: record the trade in the tradeRecord file
        '''
        stockSymbol=symbols.get(Symbol)
        stockQuantity= int(Quantity)
        indicator=indicatorMap.get(ind)
        stockTradePrice=float(tradePrice)

        if not os.path.getsize("tradeRecord") == 0:
            with(open('tradeRecord','r')) as f:
                listRecord=[ f.read()]
        else:
            listRecord = []


        try:
            recordData=TradeData(stockSymbol,stockQuantity,indicator,stockTradePrice,datetime.now())
            listRecord.append(recordData.tradeDetails())
            with open('tradeRecord','w') as f:
                f.write('\n'.join(listRecord))

            print 'Trade Record : ',recordData.tradeDetails()
        except EOFError:
            pp('No print Data')
        finally:
            f.close()


    def volumeWeightedStockPrice(self,Symbol):

        '''
        Calculation of voumne weighted stock price in last 5 mins
        :param stockSymbol:
        :return: volumeWeightedStockPrice
        '''
        stockSymbol=symbols.get(Symbol)
        tradeTime = datetime.now()-timedelta(minutes=5)
        totalQuantity = 0
        totalstockPrice=0

        listRecord =[]

        if not os.path.getsize('tradeRecord')==0:

            with open('tradeRecord') as f:
                for line in  f.read().splitlines():
                    listRecord.append(line)
        stockQuantity = int(float((listRecord[1][17:]).rstrip()))


        for j in range(0,len(listRecord)+1,5):
            try:
                if j + 1 > len(listRecord):
                    break

                elif datetime.strptime(listRecord[j+4][-26:],"%Y-%m-%d %H:%M:%S.%f" ) > tradeTime and (listRecord[j][-4:]).rstrip() == stockSymbol:
                    totalQuantity += int(float((listRecord[j+1][17:]).rstrip()))
                    totalstockPrice += int(float((listRecord[j+3][19:]).rstrip()))
            except IndexError:
                pass
        volumeWeightedStockPrice = 0

        if totalstockPrice > 0 and totalQuantity > 0:
            for key in symbols.keys():

                volumeWeightedStockPrice = (totalstockPrice * stockQuantity)/totalQuantity
                #print 'Volumen Weighted Stock Price: ',float(volumeWeightedStockPrice)
        return volumeWeightedStockPrice





    def shareIndex(self):

        '''
        Share index calculation
        :return: prints the share index
        '''

        listRecord = []

        if not os.path.getsize('tradeRecord') == 0:
            with open('tradeRecord') as f:
                for line in f.read().splitlines():
                    listRecord.append(line)

        items= len(listRecord)+1
        root= items/5
        sum = 0

        for key in symbols.keys():
            sum += self.volumeWeightedStockPrice(key)


        if sum >0 and root >0:
            gbceShareIndex = sum ** (1/root)
            print'Share Index: ', gbceShareIndex
        else:
            print 'No trade records'
















