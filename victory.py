# Викторина
greeting = 'Добро пожаловать на викторину! "Великие писатели'
print(greeting)
condition = 'Назовите года писателей!'
print(condition)

print('')
# Правильный ответ: год рождения А.И. Куприн - 1870
print('Вопрос 1: Какого года рождения А.И. Куприн?')
answer1 = int(input('Ответ: '))
# Правильный ответ: год рождения Н.В. Гоголь - 1809
print('Вопрос 2: Какого года рождения Н.В. Гоголь?')
answer2 = int(input('Ответ: '))
# Правильный ответ: год рождения А.П. Чехов - 1860
print('Вопрос 3: Какого года рождения А.П. Чехов?')
answer3 = int(input('Ответ: '))
# Правильный ответ: год рождения А.С. Пушкин - 1799
print('Вопрос 4: Какого года рождения А.С. Пушкин?')
answer4 = int(input('Ответ?: '))
# Правильный ответ: год рождения М.Ю. Лермонтов - 1814
print('Вопрос 5: Какого года рождения М.Ю. Лермонтов?')
answer5 = int(input('Ответ: '))
# Правильный ответ: год рождения Н.А. Некрасов - 1821
print('Вопрос 6: Какого года рождения Н.А. Некрасов?')
answer6 = int(input('Ответ: '))
# Правильный ответ: год рождения И.С. Тургенев - 1818
print('Вопрос 7: Какого года рождения И.С. Тургенев?')
answer7 = int(input('Ответ: '))
# Правильный ответ: год рождения Л.Н. Толстой - 1828
print('Вопрос 8: Какого года рождения Л.Н. Толстой?')
answer8 = int(input('Ответ: '))
# Правильный ответ: год рождения И.А. Гончаров - 1812
print('Вопрос 9: Какого года рождения И.А. Гончаров?')
answer9 = int(input('Ответ: '))

print('')
# Расчеты
right_answer = 0
wrong_answer = 0
if answer1 == 1870:
    right_answer += 1
else:
    wrong_answer += 1
if answer2 == 1809:
    right_answer += 1
else:
    wrong_answer += 1
if answer3 == 1860:
    right_answer += 1
else:
    wrong_answer += 1
if answer4 == 1799:
    right_answer += 1
else:
    wrong_answer += 1
if answer5 == 1814:
    right_answer += 1
else:
    wrong_answer += 1
if answer6 == 1821:
    right_answer += 1
else:
    wrong_answer += 1
if answer7 == 1818:
    right_answer += 1
else:
    wrong_answer += 1
if answer8 == 1828:
    right_answer += 1
else:
    wrong_answer += 1
if answer9 == 1812:
    right_answer += 1
else:
    wrong_answer += 1

print('')
# Результаты
print('Результаты')
print('')
print('Правильных ответов', right_answer)
print('Неправильных ответов', wrong_answer)
print('Процент правильных ответов', right_answer * 100 / 9)
print('Процент неправильных ответов', wrong_answer * 100 / 9)

print('')
# Сыграть ещё раз
questions = input('Желаете сыграть ещё раз?(да/нет): ')
