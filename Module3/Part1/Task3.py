def digits_sum(num):
    total = 0
    num = str(num)
    for i in range(len(num)):
        total += int(num[i])
    return total

number = int(input())
print(digits_sum(number))