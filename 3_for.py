"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    product_list = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}
    ]

    for product in product_list:
        sum_items_sold = 0
        count_items_sold = len(product['items_sold'])
        for items in product['items_sold']:
            sum_items_sold += items
        product['sum_items_sold'] = sum_items_sold
        product['count_items_sold'] = count_items_sold
        product['averange_items_sold'] = sum_items_sold / count_items_sold

    sum_all_items_sold = 0
    count_all_items_sold = 0
    for product in product_list:
        sum_all_items_sold += product['sum_items_sold']
        count_all_items_sold += product['count_items_sold']
    averange_all_items_sold = sum_all_items_sold / count_all_items_sold

    # * вывести суммарное количество продаж для каждого товара
    for product in product_list:
        print(product['product'], product['sum_items_sold'])

    # * вывести среднее количество продаж для каждого товара
    for product in product_list:
        print(product['product'], product['averange_items_sold'])

    # * вывести суммарное количество продаж всех товаров
    print(sum_all_items_sold)

    # * вывести среднее количество продаж всех товаров
    print(averange_all_items_sold)


if __name__ == "__main__":
    main()
