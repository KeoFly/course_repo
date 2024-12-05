from random import randint

def max_num(m):
    num = 0
    for i in m:
        for j in i:
            if num < j:
                num = j
    return num

n = 5
m = [[randint(0, 100) for i in range(n)] for j in range(n)]

print(max_num(m))