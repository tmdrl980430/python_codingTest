# A -> B

# 가능한 연산
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.

# A 를 B로 바꾸는데 필요한 연산의 최솟값을 구하기

#반대로 생각해서 더 큰수인 B에서 A로 만들기 위한 코드를 작성한다.

A, B = map(int, input().split())

answer = 1
while A != B:
    answer += 1
    if B % 10 == 1:
        B //= 10
    else:
        if B % 2 == 1:
            answer = -1
            break
        else:
            B //= 2
    if B < A:
        answer = -1
        break

print(answer)
            
    