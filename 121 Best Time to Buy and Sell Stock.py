prices=[7,1,5,3,6,4]

def maxProfit(prices):
	if len(prices) == 0:
		return 0
	else:
		low = 999999999
		maxProfit = 0

		for price in prices:
			if price > low:
				if price - low > maxProfit:
					maxProfit = price - low
			else:
				low = price
	return maxProfit

print(maxProfit(prices))