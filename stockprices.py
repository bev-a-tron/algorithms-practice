# stock prices from interviewcake

# stockprices[i] is an nx1 array with one company's stock price information for each minute of the day.
# write an algorithm to maximize the profit from one buy, one sell.
# no shorting allowed.

def get_max_profit(stockprices):
	max_profit = 0
	for i in range(len(stockprices)):
		lowest = min(stockprices[0:i+1])
		highest = max(stockprices[i:len(stockprices)+1])
		this_profit = highest - lowest
		if this_profit > max_profit:
			max_profit = this_profit
	return max_profit

if __name__ == "__main__":
	ans = get_max_profit([30,10,100,5,20,500,900,10,20,1])
	print "The max profit is: $%u"%(ans)