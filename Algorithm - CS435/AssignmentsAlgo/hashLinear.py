A = [None, None, 2, 41, None, None, 18, 44, 59, 32, 22, 31, 73, None]
#N = len(A)
N = 13

def findValue(k):
    item = findItem(k) 
    return item 

def hash(k):
    return k % N


def findItem(k): 
    i = hash(k)
    p = 0 
    while p < N:
        x = (i+p) % N
        item = A[x]
        if not item:
            return "no such key" 
        elif item == k:
            return x
        else: 
            p = p + 1
        
        return "NO_SUCH_KEY"


print(findValue(2))


