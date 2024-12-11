a = [1, 2, 3, 4, 5, 6]

def binary(a, number):
    centre = int(len(a) / 2)
    centre_num = a[int(len(a) / 2)]
    if centre_num == number:
        return centre_num
    elif centre_num > number:
        return binary(a[:centre], number)
    else:
        return binary(a[centre:], number)

print(binary(a, 6))