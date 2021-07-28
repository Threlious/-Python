nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=False):
    """
    get_jokes генерирует сочетания из 3 слов из каждого из 3 списков (nouns, adverbs, adjectives) в количестве n,
    указанным пользователем. Повторы слов регулируются аргументом flag, который по умолчанию равен false
    (шутки с повторами)
    """
    from random import choice, randrange
    list_jokes = []
    i = 1
    noun_nonrep, adverb_nonrep, adjective_nonrep = nouns.copy(), adverbs.copy(), adjectives.copy()
    joke_min = min(noun_nonrep, adverb_nonrep, adjective_nonrep)  # оставшийся размер списка
    while i <= n:
        last = randrange(len(joke_min))
        if not flag:  # шутки с повтором
            list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        else:  # шутки без повторов
            list_jokes.append(f'{noun_nonrep.pop(last)} {adverb_nonrep.pop(last)} {adjective_nonrep.pop(last)}')
        i += 1
    return list_jokes


print(get_jokes(6))
print(get_jokes(4, True))
