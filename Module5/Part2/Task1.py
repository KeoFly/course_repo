import json

class C1:
    title = '1'
    text = '2'
    author = '3'


class Model(C1):
    def save(self, file="data.json"):
        data_dict = dict.fromkeys(dir(C1))
        with open("data.json", "w") as f:
            json.dump(data_dict, f)

a = Model()
a.save()