
def findWinner(s):
    if not s:
        return None
    dict = {}
    dict[s[0]] = 1
    i = 0
    while i < len(s) - 1: 
        el = s[i]
        i += 1
        if el in dict:
            dict[el] = dict[el] + 1
        else: 
            dict[el] = 1

    return findWinHelper(dict, 0)

def findWinHelper(dict, index):
    keys = list(dict.keys())
    if index < len(keys): 
        key = keys[index]
        return dict[key] + findWinHelper(dict, index + 1)
    else:
        return 0


print(findWinner([2,3,2,1,2,2]))