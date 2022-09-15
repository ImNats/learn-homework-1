"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

questions_and_answers = {
    'Привет': 'Привет!',
    'Как дела?': 'Хорошо!',
    'Как жизнь?': 'Хорошо!',
    'Что делаешь?': 'Программирую',
    'Какая завтра погода?': 'Дождливая!',
    'Что умеешь?': 'Отвечать на вопросы!',
    'Завтра будет гроза?': 'Сейчас не май, не будет!',
    'Как провел лето?': 'Валялся на пляже!'
}


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    text_input = input('Задай мне вопрос, я постараюсь на него ответить? ')
    try:
        while True:
            if questions_and_answers.get(text_input) is not None:
                print(questions_and_answers[text_input])
            text_input = input('Попробуй еще спросить! ')
    except KeyboardInterrupt:
        print('\nПока')


if __name__ == "__main__":
    ask_user(questions_and_answers)
