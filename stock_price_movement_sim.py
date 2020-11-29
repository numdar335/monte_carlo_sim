import datetime
import matplotlib.pyplot
import numpy
import pandas
from pandas_datareader import data
from scipy.stats import norm

def check(date):
  if len(date) != 10 or date[4] != '-' or date[7] != '-':
    print("Invalid input.")
    return True
  else:
    for i in range(1, 10):
      if i != 5 and i != 8 and (ord(date[i-1])-48 < 0 or ord(date[i-1])-48 > 9):
        print("Invalid input.")
        return True
    return False

corpName = raw_input("Insert corporation name: ")
stockSymbol = raw_input("Insert stock symbol: ")
helperVar = True
while helperVar:
  date1 = raw_input("Insert first day (format: 'YYYY-MM-DD'): ")
  helperVar = check(date1)
helperVar = True
while helperVar:
  date2 = raw_input("Insert final day (format: 'YYYY-MM-DD'): ")
  helperVar = check(date2)
simulations = input("Insert number of simulations: ")
days = (datetime.datetime.strptime(date2,"%Y-%m-%d").date()-datetime.datetime.strptime(date1,"%Y-%m-%d").date()).days+1
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
matplotlib.pyplot.title("%i "%simulations+"possible movements of %s's "%corpName+"stock prices after %s "%date1+"(assuming that the Efficient Market Hypothesis holds)")
matplotlib.pyplot.xlabel("Days")
matplotlib.pyplot.ylabel("Price (currency depends on stock exchange)")
matplotlib.pyplot.plot(prices)
print("Results displayed. End of program.")
matplotlib.pyplot.show()
