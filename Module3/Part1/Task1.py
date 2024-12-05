def deposit(x, y, p):
    count_year = 0
    while x < y:
        x = int(x)
        x += x * (p / 100)
        count_year += 1
    return count_year

x, y, p = int(input()), int(input()), int(input())
print(deposit(x, y, p))