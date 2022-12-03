#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

# Задача №1
if __name__ == '__main__':
    shops = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            name = input("Название магазина ")
            product = input("Товар ")
            price = float(input("Цена "))
            shop = {
                'name': name,
                'product': product,
                'price': price,
            }
            shops.append(shop)
            if len(shops) > 1:
                shops.sort(key=lambda item: item.get('name', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 8,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "No",
                    "Название.",
                    "Товар",
                    "Цена"
                )
            )
            print(line)
            for idx, shop in enumerate(shops, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        shop.get('name', ''),
                        shop.get('product', ''),
                        round(shop.get('price', 0), 2)
                    )
                )
                print(line)
        elif command == 'select':
            sname = input("Название магазина ")
            cout = 0
            for shop in shops:
                if (shop.get('name') == sname):
                    cout = 1
                    print(
                        ' | {:<5} | {:<5} '.format(
                            shop.get('product', ''),
                            round(shop.get('price', 0), 2),
                        )
                    )
                elif cout == 0:
                    print("Такого магазина нет")
        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить магазин;")
            print("select - показать товары из заданного магазина;")
            print("list - вывести список магазинов;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
