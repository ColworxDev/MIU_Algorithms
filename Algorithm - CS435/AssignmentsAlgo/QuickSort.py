import random

def inPlaceQuickSort(S, l, r):

    def swapElements(lo, hi):
        t = S[lo]
        S[lo] = S[hi]
        S[hi] = t
        
    def inPlacePartition(S, lo, hi):
        

        p = random.randint(lo, hi)
        swapElements(lo, p)
        pivot = S[lo]

        j = lo + 1
        k = hi

        while j <= k:
            while (k >= j and S[k] >= pivot):
                k = k - 1
            while (j <= k and S[j] <= pivot):
                j = j + 1
            if j < k:    
                swapElements(j, k)

        swapElements(lo, k)
        return k
    
    if l < r:
        p = inPlacePartition(S, l, r)
        inPlaceQuickSort(S, l, p - 1)
        inPlaceQuickSort(S, p + 1, r)
    return S

    


    
        

print(inPlaceQuickSort([2,3,4,7,2,1,4,9], 0, 7))