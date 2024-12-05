def max_num(list):
    tmp_list = []
    for i in range(len(list)):
        num1 = 0
        num2 = 0
        result = ''

        for j in range(len(list)):
            num2 = list[j]
            num21 = list[j]
            num11 = num1

            while num21 >= 10:
                num21 //= 10
            while num11 >= 10:
                num11 //= 10

            if num2 not in tmp_list and num1 not in tmp_list:
                if num2 < 10:
                    if num11 < num2:
                        num1 = num2
                elif num1 > 10 and num2 > 10:
                    if num11 <= num21 and num1 < num2:
                        num1 = num2
                else:
                    if num1 < num21:
                        num1 = num2

        tmp_list.append(num1)
    for num in tmp_list:
        result += str(num)
    return int(result)

list = [3, 81, 5]
list2 = [56, 9, 11, 2]
print(max_num(list2))