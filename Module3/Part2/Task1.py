def repeating_elements(list):
    l_elements = []
    for i in list:
        if list.count(i) > 1:
            l_elements.append(i)

    return l_elements


l = [1, 4, 1, 6, "hello", "a", 5, "hello"]

print(repeating_elements(l))