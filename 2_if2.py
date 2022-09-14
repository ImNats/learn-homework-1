"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main(text_input_1, text_input_2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if type(text_input_1) != str or type(text_input_2) != str:
        text_output = 0
    elif text_input_1 == text_input_2:
        text_output = 1
    elif len(text_input_1) > len(text_input_2):
        text_output = 2
    elif text_input_2 == 'learn':
        text_output = 3
    else:
        text_output = None

    return text_output


text_input_1 = 1
text_input_2 = ''
print(main(text_input_1, text_input_2))
text_input_1 = ''
text_input_2 = 5,5
print(main(text_input_1, text_input_2))
text_input_1 = 'gg'
text_input_2 = 'gg'
print(main(text_input_1, text_input_2))
text_input_1 = 'gg'
text_input_2 = 'hh'
print(main(text_input_1, text_input_2))
text_input_1 = 'gggg'
text_input_2 = 'hh'
print(main(text_input_1, text_input_2))
text_input_1 = 'gggg'
text_input_2 = 'learn'
print(main(text_input_1, text_input_2))
text_input_1 = 'learn'
text_input_2 = 'learn'
print(main(text_input_1, text_input_2))
text_input_1 = 'learnlearn'
text_input_2 = 'learn'


if __name__ == "__main__":
    main(text_input_1, text_input_2)
