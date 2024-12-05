def switch_val(d):
    keys = list()
    values = list()
    for key, value in d.items():
        keys.append(key)
        values.append(value)
    d.clear()
    for i in range(len(keys)):
        d[values[i]] = keys[i]
    return d

d = {"name1": "id1", "name2": "id2", "name3": "id3"}
print(switch_val(d))