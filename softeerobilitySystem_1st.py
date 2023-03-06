import sys

n , t =  map(int, sys.stdin.readline().split())

matrix = [[0 for x in range(4)] for z in range(n*n)]
cross_street = [[0 for x in range(n)] for z in range(n*n)]
for i in range(n):
    for z in range(n*n):
        cross_street[z][i] = [i+1, z+1]

traffic_x1 = [-1,1,0,0]
traffic_y1 = [0,0,1,-1]

traffic_light_dict = {}
for i in range(n*n):
    temp_arr = list(map(int, sys.stdin.readline().split()))
    traffic_light_dict[i+1] = temp_arr

