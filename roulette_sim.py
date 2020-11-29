import matplotlib.pyplot
from random import randint

def martingale(initBankroll,initBet):
  print("Simulating (a slightly modified version of) the Martingale strategy...")
  x, y = [], []
  bankroll, currBet, counter = initBankroll, initBet, 0
  while bankroll >= currBet:
    x.append(counter)
    y.append(bankroll)
    if not randint(0,36)%2:
      bankroll -= currBet
      currBet = 2*currBet
    else:
      bankroll += currBet
      currBet = initBet
    if 0 < bankroll < currBet: currBet = bankroll
    counter += 1
  matplotlib.pyplot.plot(x,y)

def dAlembert(initBankroll,initBet):
  x, y = [], []
  print("Simulating (a slightly modified version of) the d'Alembert strategy...")
  bankroll, currBet, counter = initBankroll, initBet, 0
  while bankroll >= currBet:
    x.append(counter)
    y.append(bankroll)
    if not randint(0,36)%2:
      bankroll -= currBet
      currBet += initBet
    else:
      bankroll += currBet
      if currBet != initBet: currBet -= initBet
    if 0 < bankroll < currBet: currBet = bankroll
    counter += 1
  matplotlib.pyplot.plot(x,y)

def pluscoup(initBankroll,initBet):
  print("Simulating (a slightly modified version of) the Pluscoup progression...")
  x, y = [], []
  bankroll, currBet, counter = initBankroll, initBet, 0
  while bankroll >= currBet:
    x.append(counter)
    y.append(bankroll)
    if not randint(0,36)%2: bankroll -= currBet
    else:
      bankroll += currBet
      currBet += initBet
    if 0 < bankroll < currBet: currBet = bankroll
    counter += 1
  matplotlib.pyplot.plot(x,y)

def kelly(initBankroll,initBet):
  print("Simulating (a slightly modified version of) the Kelly criterion...")
  x, y = [], []
  bankroll, counter = initBankroll, 0
  helperVar = False
  while bankroll >= 0.01:
    x.append(counter)
    y.append(bankroll)
    if not helperVar:
      currBet = initBet
      helperVar = True
    else: currBet = bankroll*(18/37.0+(1-18/37.0)/(19/18.0))
    if randint(0,36)%2: bankroll -= currBet
    else: bankroll += currBet
    counter += 1
  matplotlib.pyplot.plot(x,y)

while True:
  initBankroll = input("Insert bankroll: ")
  if initBankroll <= 0: print("Invalid input (your bankroll needs to be greater than zero).")
  else: break
while True:
  initBet = input("Insert initial bet: ")
  if initBet > initBankroll: print("Invalid input (your initial bet can't be larger than your initial bankroll).")
  elif initBet <= 0: print("Invalid input (your initial bet needs to be greater than zero).")
  else: break
print("Choose at least one gambling strategy out of the following (input examples: '1', '12', '412', '2431'):\n1. Martingale\n2. d'Alembert\n3. Pluscoup\n4. Kelly")
checkVar = False
while not checkVar:
  checkVar = True
  str = raw_input()
  checkArr = [False, False, False, False]
  for i in range(1,len(str)+1):
    if str[i-1] != '1' and str[i-1] != '2' and str[i-1] != '3' and str[i-1] != '4':
      print("Invalid characters in input.")
      checkVar = False
    else: checkArr[int(str[i-1])-1] = True
if checkArr[0]: martingale(initBankroll,initBet)
if checkArr[1]: dAlembert(initBankroll,initBet)
if checkArr[2]: pluscoup(initBankroll,initBet)
if checkArr[3]: kelly(initBankroll,initBet)
print("All simulations completed.\nAdding a few finishing touches to your results...")
matplotlib.pyplot.xlabel("Number of bets")
matplotlib.pyplot.ylabel("Bankroll")
print("Results displayed. End of program.")
matplotlib.pyplot.show()
