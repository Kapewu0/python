from itertools import chain

primaryList = [[2,4,3], [1,5,6], [9], [7,9,0]]
res = list(chain.from_iterable(primaryList))
print(res)