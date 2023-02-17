arr = []
for i in range(1, 10001):
    sum = 0
    sum += i
    a = str(i)
    for j in range(len(a)):
        sum += int(a[j])
    arr.append(sum)
temp = 1
while temp < 10000:
    if temp in arr:
        temp += 1
        continue
    else:
        print(temp)
        temp += 1