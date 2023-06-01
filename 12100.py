from collections import deque
import copy

# 보드 초기화
def initialize_board(n):
    board = []
    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)
    return board

# 보드 출력
def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

# 보드 이동
def move(board, direction, n):
    if direction == 'left':
        for row in board:
            merge_row(row , n)
    elif direction == 'right':
        for row in board:
            row.reverse()
            merge_row(row, n)
            row.reverse()
    elif direction == 'up':
        for col in range(n):
            column = [board[row][col] for row in range(n)]
            merge_row(column, n)
            for row in range(n):
                board[row][col] = column[row]
    elif direction == 'down':
        for col in range(n):
            column = [board[row][col] for row in range(n-1, -1, -1)]
            merge_row(column, n)
            for row in range(n-1, -1, -1):
                board[row][col] = column[n-1 - row]

# 행 또는 열 병합
def merge_row(row, n):
    for i in range(n - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0

# 보드 복사
def copy_board(board):
    return [row[:] for row in board]

# 최댓값 계산
def get_max_value(board):
    max_value = 0
    for row in board:
        max_value = max(max_value, max(row))
    return max_value

# BFS로 보드 이동 시뮬레이션
def bfs(board, n):
    queue = deque([(board, 0)])  # (보드, 이동 횟수)를 큐에 저장
    max_value = 0

    while queue:
        current_board, depth = queue.popleft()

        max_value = max(max_value, get_max_value(current_board))

        if depth == 5:  # 최대 깊이에 도달한 경우
            continue

        for direction in ['left', 'right', 'up', 'down']:
            copied = copy_board(current_board)
            move(copied, direction, n)
            queue.append((copied, depth + 1))

    return max_value

# 메인 함수
n = int(input())
board = initialize_board(n)
answer = bfs(board , n)
print(answer)

