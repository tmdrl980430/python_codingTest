a = int(input())

sum = 0
i = 1
while sum <= a:
    sum += i
    if sum + i >= a:
        break
    i += 1

print(i)