N = 11
list_new = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
print ("----------- R-2.21 --------------")
def hash_get(k):
    return (2*k+5) % N
def prepareHashLinear(l):
    New_List = [None] * (N)
    #New_List_Index = {}
    ii = 0
    for j in range(0, len(l)):
        i = hash_get(l[j])
        #New_List_Index[ii] = {'EL': l[j], 'index':i}
        #ii+=1
        if New_List[i]:
            p = 0
            x = i
            while New_List[x]!=None:
                p += 1
                x = (i + p*p) % N
                print (l[j],x)
            New_List[x] = l[j]
        else:
            New_List[i] = l[j]
    return New_List,New_List_Index
A,AA = prepareHashLinear(list_new)
print ("prepareHashLinear:\n",A,'\n',AA)

# def findValueLinear(k):
#     item = findItemLinear(k)
#     return item

# def findItemLinear(k):
#     i = hash_get(k)
#     p = 0
#     cnt = 0
#     while p < N:
#         x = (i + p*p) % N
#         item = A[x]
#         cnt += 1
#         if not item:
#             return "NO_SUCH_KEY"
#         elif item == k:
#             return cnt
#         else:
#             p = p + 1
#     return "NO_SUCH_KEY"

# sumS = 0
# for ii in list_new:
#     sumS+=findValueLinear(ii)
#     print (A," VAL:",ii,"  index:",findValueLinear(ii))
# print (sumS)
