

A = [1,2,3]
B = [1,2,3]
C = []



def combineTwo():
    print(C)
    return combineHelper(1, A[0])

def combineHelper(i, element):
    
    if A[i] == element:
        C += combineHelper(i+1, element)
    if A[i] != B[i]:
        C += A[i]
    C += combineHelper(i+ 1, element)
    






combineTwo()
print(C)