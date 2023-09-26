n = int(input())

result = 0

for i in range(1,n):
    temp1 = i
    sum = i
    while True:
        if temp1 == 0:
            break
        if temp1 > 0:
            sum = sum + (temp1%10)
            temp1 = temp1 // 10

    if sum == n:
        result = i
        break

print(result)