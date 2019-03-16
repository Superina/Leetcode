def powerset(input):
    result = ['']

    def helper(i):
        if i >= len(input):
            return
        else:
            result.extend([item + input[i] for item in result])
        helper(i+1)

    helper(0)
    return result