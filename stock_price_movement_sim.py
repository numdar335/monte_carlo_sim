import datetime
import matplotlib.pyplot
import numpy
import pandas
from pandas_datareader import data
from scipy.stats import norm

def formatCheck(date):
  if len(date) != 10 or date[4] != '-' or date[7] != '-':
    print("Wrong format.")
    return False
  else:
    for i in range(1, 11):
      if i != 5 and i != 8 and (ord(date[i-1])-48 < 0 or ord(date[i-1])-48 > 9):
        print("Wrong format.")
        return False
    return True

corpName = raw_input("Insert corporation name: ")
stockSymbol = raw_input("Insert stock symbol: ")
helperVar = False
while not helperVar:
  date1 = raw_input("Insert first day (make sure that the date is valid). Format: 'YYYY-MM-DD': ")
  helperVar = formatCheck(date1)
helperVar = False
while not helperVar:
  date2 = raw_input("Insert final day (make sure that the date is valid). Format: 'YYYY-MM-DD': ")
  helperVar = formatCheck(date2)
  if helperVar:
    days = (datetime.datetime.strptime(date2,"%Y-%m-%d").date()-datetime.datetime.strptime(date1,"%Y-%m-%d").date()).days+1
    if days-1 <= 0:
      print("The date you inserted is not later than "+date1+".")
      helperVar = False
simulations = input("Insert number of simulations: ")
stockData = pandas.DataFrame()
stockData[stockSymbol] = data.DataReader(stockSymbol,"yahoo",date1)['Adj Close']
periodicDailyReturn = numpy.log(stockData.pct_change()+1)
drift = periodicDailyReturn.mean()-periodicDailyReturn.var()/2
standardDeviation = periodicDailyReturn.std()
helper = numpy.exp(drift.values+standardDeviation.values*norm.ppf(numpy.random.rand(days,simulations)))
prices = numpy.zeros_like(helper)
prices[0] = stockData.iloc[-1]
for i in range(2,days+1): prices[i-1] = prices[i-2]*helper[i-1]
matplotlib.pyplot.figure(figsize=(18,9))
matplotlib.pyplot.title("%i "%simulations+"possible movements of %s's "%corpName+"stock prices after %s "%date1+"(assuming that the efficient market hypothesis holds)")
matplotlib.pyplot.xlabel("Days")
matplotlib.pyplot.ylabel("Price (currency depends on stock exchange)")
matplotlib.pyplot.plot(prices)
print("Results displayed. End of program.")
matplotlib.pyplot.show()
