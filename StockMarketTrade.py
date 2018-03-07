from  StockCalculations import StockCalculations

'''
Its the main function. 

:param argv: arguments from the command line

'''


option = 0
while True:
    print ("****************************")
    option = input("Enter your choice:" +
                       "\n***********************************" +
                       "\n| 1 | dividend yield" +
                       "\n| 2 | P/E Ratio" +
                       "\n| 3 | Record Trade" +
                       "\n| 4 | Volume Weighted Stock Price " +
                       "\n| 5 | Stock Index" +
                       "\n*************************************\n>")

    if(option == '1'):
        print("****************************")
        symbol = input("Choose a stock symbol:" +
                           "\n| 1 | TEA " +
                           "\n| 2 | POP " +
                           "\n| 3 | ALE " +
                           "\n| 4 | GIN " +
                           "\n| 5 | JOE \n" +
                           "**********************************\n>").isupper()

        price = input("Enter the stock price \n")
        print ("***********************************")

        dividend = StockCalculations().dividendCalc(symbol, price)

        print ("Dividend Yield : ", dividend)

        print ("*****************************************")
        print ("\n \n")

    elif(option == '2'):
        symbol = input("Choose a stock symbol:" +
                           "\n| 1 | TEA " +
                           "\n| 2 | POP " +
                           "\n| 3 | ALE " +
                           "\n| 4 | GIN " +
                           "\n| 5 | JOE \n" +
                           "************************************\n>")

        price = input("Enter the stock price \n")
        print ("*********************************")

        peratio = StockCalculations().peRatioCalc(symbol, price)

        print ("P/E Ratio : ", peratio)

        print ("*****************************************")
        print ("\n \n")

    elif(option == '3'):
        symbol = input("Choose a stock symbol:" +
                           "\n| 1 | TEA " +
                           "\n| 2 | POP " +
                           "\n| 3 | ALE " +
                           "\n| 4 | GIN " +
                           "\n| 5 | JOE \n" +
                           "*******************************************\n>")

        quantity = input("Quantity of stocks \n")

        indicator = input("Choose a indicator :" +
                              "\n| 1 | BUY " +
                              "\n| 2 | SELL \n" +
                              "******************************************\n>")

        stockTradePrice = input("Enter stock price \n")


        StockCalculations().tradeRecord(stockSymbol, stockQuantity, indicator, stockTradePrice)

        print ("****************************************")
        print ("\n \n")

    elif(option == '4'):
        symbol = input("Choose a stock symbol:" +
                           "\n| 1 | TEA " +
                           "\n| 2 | POP " +
                           "\n| 3 | ALE " +
                           "\n| 4 | GIN " +
                           "\n| 5 | JOE \n" +
                           "**************************************\n>")

        print ("*****************")

        StockCalculations().volumeWeightedStockPrice(symbol)

        print ("*****************************************")
        print ("\n \n")

    elif(option == '5'):
        StockCalculations().shareIndex()

        print( "*****************************************")
        print ("\n \n")
