# monte_carlo_sim

At the [National Kapodistrian University of Athens](https://en.wikipedia.org/wiki/National_and_Kapodistrian_University_of_Athens), I'm currently enrolled in a postgraduate course about [reinforcement learning](https://www.amazon.com/Reinforcement-Learning-Introduction-Adaptive-Computation/dp/0262039249) and [stochastic games](https://www.amazon.com/Competitive-Markov-Decision-Processes-Jerzy/dp/0387948058), and in a seminar about [Monte Carlo statistical methods](https://www.amazon.com/Monte-Statistical-Methods-Springer-Statistics-dp-1441919392/dp/1441919392). In both of these two courses, I've come across the term "Monte Carlo simulation" multiple times, so I read up on it a little, and I decided that it would be fun to make a software repository, containing implementations of a few Monte Carlo simulators. So far, I have included a [stock price movement simulator](https://en.wikipedia.org/wiki/Stock_market_prediction) and a [roulette simulator](https://en.wikipedia.org/wiki/Roulette), and I will soon start working on a few others, which I'm actually very excited about.

## Roulette Simulator

The roulette simulator can be used in order to compare the effectiveness of various gambling strategies. It is European-style: we assume that the wheel has 37 pockets (in American roulette, the wheel has 38 pockets, in order to increase the [house edge](https://en.wikipedia.org/wiki/Casino_game#House_advantage)). We also assume that the bet is on odd-numbered pockets, so that the probability of winning is as high as possible (sidenote: there are other bets with equally high probability of winning, such as betting on even-numbered pockets, red pockets, black pockets etc).

So far, the only gambling strategies available for simulation are the <ins>Martingale system</ins>, the <ins>d'Alembert system</ins>, the <ins>Pluscoup progression</ins> and the <ins>Kelly criterion</ins>. All of them have been slightly modified (for various reasons), for example the Pluscoup algorithm won't stop when profit is generated; it won't stop until the bettor completely runs out of money (otherwise the data representation will look really bad). Another example: the Kelly algorithm won't use the Kelly percentage to determine the value of the first bet (in my opinion the simulator is much nicer when the user decides the value of the initial bet, which is then taken into consideration by all four algorithms). Another example is that no algorithm stops when the bankroll is smaller than the bet that the algorithm considers to be optimal. Instead, the entire remaining bankroll is placed as a bet, and the simulation continues.

## Stock Price Movement Simulator

This simulator is a lot simpler than the previous one, and it was also a lot easier for me to implement, since I basically just followed [this article](https://www.investopedia.com/terms/m/montecarlosimulation.asp).
