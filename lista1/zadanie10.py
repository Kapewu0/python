numbers = list(range(3, 100, 3))
print(numbers)

del numbers[4:(len(numbers)-1):3]
print(numbers)

mean = sum(numbers) / len(numbers)
print(mean)