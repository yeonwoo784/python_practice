n = int(input())
numbers = list(map(int, input().split())) #n개 값을 받아야할 때 list로 나열, map과split으로 여러개 받기.
print(min(numbers), max(numbers))