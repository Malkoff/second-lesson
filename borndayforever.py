# цикл год и день рождения А.С. Пушкина

answer_one = int(input('Какой год рождения А.С. Пушкина? '))

while answer_one != 1799:
    answer_one = int(input('Какой год рождения А.С Пушкина? '))
if answer_one == 1799:
    answer_two = int(input('Какой день рождения А.С. Пушкина? '))
    while answer_two != 6:
        answer_two = int(input('Какой день рождения А.С. Пушкина? '))
    if answer_two == 6:
        print('Верно')