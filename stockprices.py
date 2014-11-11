# stock prices from interviewcake

# Writing interview questions hasn't made me rich. Maybe trading Apple stocks will.
# I have an array stockPricesYesterday where:
# The indices are the time, as a number of minutes past trade opening time, which was 9:30am local time.
# The values are the price of Apple stock at that time, in dollars.
# For example, the stock cost $500 at 10:30am, so stockPricesYesterday[60] = 500.
# Write an efficient algorithm for computing the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday. For this problem, we won't allow "shorting"—you must buy before you sell.

def get_max_profit(stockprices):
	max_profit = 0
	for i in range(len(stockprices)):
		lowest = low(stockprices, 0, i)
		highest = high(stockprices, i, len(stockprices))
		this_profit = highest - lowest
		if this_profit > max_profit:
			max_profit = this_profit
	return max_profit

def low(stockprices, left, right):
	lowest_price = stockprices[0]
	for i in range(left, right):
		if stockprices[i] < lowest_price:
			lowest_price = stockprices[i]
	return lowest_price

def high(stockprices, left, right):
	highest_price = stockprices[-1]
	for i in range(left, right):
		if stockprices[i] > highest_price:
			highest_price = stockprices[i]
	return highest_price


if __name__ == "__main__":
	ans = get_max_profit([30,10,100,20,500])
	print "The max profit is: $%u"%(ans)