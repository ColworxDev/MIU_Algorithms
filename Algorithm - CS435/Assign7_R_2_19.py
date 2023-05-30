N = 11
list_new = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
print ("----------- R-2.19 --------------")
def hash_get(k):
    return (2*k+5) % N
def prepareHashChaning(l):
    New_dict = {}
    for j in range(0, len(l)):
        i = hash_get(l[j])
        if i in New_dict:
            New_dict[i].append(l[j])
        else:
            New_dict[i] = [l[j]]
    return New_dict

print ("prepareHash:\n",prepareHashChaning(list_new))