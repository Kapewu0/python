from itertools import chain

array = [[2,4,3], [1,5,6],[9],[7,9,0]]
res = list(chain.from_iterable(array))
print(res)
