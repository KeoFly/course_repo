class StringVar:

    def __init__(self, string):
        self.string = string

    def set(self):
        question = input("Какую букву в строке поменять и на какую? "
                         "(введите букву по счету и букву на которую хотите заменить")

        question = question.split()
        index = int(question[0]) - 1
        letter = question[1]

        self.string = self.string[:index] + letter + self.string[index + 1:]


    def get(self):
        print(self.string)

string = StringVar("abc")

string.set()
string.get()