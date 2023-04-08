
# n = 구역의 개수
n = int(input())

#구역의 인구 리스트
population_list = list(map(int, input().split()))

place_dict = {}

for i in range(n):
    adjacency_place = list(map(int, input().split()))
    place_dict[i + 1] = [adjacency_place]
print(place_dict)
