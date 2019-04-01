import copy
alist = [1,2]

# result = [[]]
# result = [[],[1]]
# result = [[],[1],[2],[1,2]]
# 

# The Best Way

def powerset(input):
    result = [[]]

    def helper(i):
        if i >= len(input):
            return
        else:
            
        helper(i+1)

    helper(0)
    return result


print powerset(alist)

# Pure Recursion
def subsets(alist):
	if len(alist) == 0:
		return []
	if len(alist) == 1:
		return [[],alist]
	else:
		original = subsets(alist[:-1])
		original_copy = copy.deepcopy(original)
		for i in original:
			i.append(alist[-1])
		final = original + original_copy
		return final


# DP
def subsets(alist):
	index = len(alist)
	if index == 0:
		return []
	else:
		memo = [None] * (index+1)
		memo[0] = []
		memo[1] = [[],[alist[0]]]
	return helper(alist,memo,index)


def helper(alist,memo,index):
	if memo[index] != None:
		return memo[index]
	else:
		original = subsets(alist[:-1])
		original_copy = copy.deepcopy(original)
		for i in original:
			i.append(alist[-1])
		final = original + original_copy
		memo[index] = final
		return memo[index]






