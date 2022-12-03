#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


def mod_list(lst):
    """""
     Принимает в качестве аргументов список и удаляет четные или нечетные значения в зависимости от параметра type
    """""
    def m_lst(typ):
        if typ == 1:
            return list(filter(lambda x: (x % 2) == 0, lst))
        elif typ == 0:
            return list(filter(lambda x: (x % 2) > 0, lst))
    return m_lst


if __name__ == '__main__':
    mylist = list(map(int, input().split()))
    a = int(input("Введите:\n 0, если хотите удалить чётные\n 1, если хотите удалить нечётные\n"))
    print(mod_list(mylist)(a))
