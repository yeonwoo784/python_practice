number = list(map(int, input().split()))
sum = 0
for i in range(len(number)):
    sum = sum + (number[i]**2)
remain = sum % 10
print(remain)