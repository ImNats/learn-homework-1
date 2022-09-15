"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


user_age = input('Привет!!! Сколько тебе полных лет?')


def main(user_age):
    # определяем подходящий тип занятия для пользователя
    if type(user_age) != int:
        user_should_do = None
    elif user_age < 0:
        user_should_do = None
    elif user_age < 7:
        user_should_do = 'учиться в детском саду'
    elif user_age < 16:
        user_should_do = 'учиться в школе'
    elif user_age < 21:
        user_should_do = 'учиться в ВУЗе'
    else:
        user_should_do = 'работать'

    # подготовить текст резолюции в выводу
    if user_should_do is None:
        resolution_text = 'Ты ошибся попробуй еще раз'
    else:
        resolution_text = f'Тебе стоит {user_should_do}'

    return resolution_text


resolution_text = main(user_age)
print(resolution_text)


if __name__ == "__main__":
    main(user_age)
