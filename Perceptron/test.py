from itertools import combinations, permutations

def subset(array_in, r):
    return list(permutations(array_in, r))

arr = [-1, 1]
out = []
for i1 in arr:
    for i2 in arr:
        for i3 in arr:
            for i4 in arr:
                out.append([i1, i2, i3, i4])
# print(out)
# r = 2
# out = subset(arr, r)

print(len(out))
for i, row in enumerate(out):
    print(i, row)

