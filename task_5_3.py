import itertools
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
if len(tutors) <= len(klasses):
    names_comb = zip(tutors, klasses)
else:
    names_comb = itertools.zip_longest(tutors, klasses)
for i in names_comb:
    print(i)
print(type(names_comb))
