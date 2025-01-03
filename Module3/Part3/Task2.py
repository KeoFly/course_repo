def words_condition(s):
    words = list()
    s = s.split()
    for word in s:
        if len(word) < 5 and word[-1] not in (",", ".", "-", "!"):
            words.append(word)
    return words


s = """было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допивая с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!"""

print(words_condition(s))