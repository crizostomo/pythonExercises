ages = [30, 29, 22, 15, 45]
for i in range (len(ages)):
    print('in the position', i, 'the age is:', ages[i])

for value in enumerate(ages):
    print(value)

for indice, age in enumerate(ages):
    print(indice, 'x', age)

print(list(reversed(ages)))
print(sorted(ages))
print(sorted(ages, reverse=True))
