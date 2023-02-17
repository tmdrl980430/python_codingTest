import sys

n = int(sys.stdin.readline())
answer = 0
confirm = True
for i in range(1, n+1):
    confirm = True
    str_i = str(i)
    str_len = len(str_i)
    for j in range(str_len):
        if j != str_len - 1:
            if j == 0:   
                temp = int(str_i[j+1]) - int(str_i[j])
                continue
            if int(str_i[j]) + temp == int(str_i[j+1]):
                continue
            else:
                confirm = False

        else:
            if confirm:
                answer += 1
print(answer)