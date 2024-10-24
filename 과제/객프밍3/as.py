numbers=[1,2,3]
for i in numbers[:]:
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)