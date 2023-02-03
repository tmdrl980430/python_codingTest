import sys

a = input()
dict = {}
for i in a:

    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        

print(dict)