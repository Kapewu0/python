n = int(input("Podaj ilość elementów szeregu Fibonacciego: \n")).__abs__()
previous = 0
current = 1
print(previous)
print(current)
for i in range(1,n+1):
    print(current + previous)
    tmp = current
    current = previous + current
    previous = tmp