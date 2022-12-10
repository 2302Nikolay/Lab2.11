#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# Индивидуальное задание вариант 1
def mod_list(lst):
    def m_lst(typ):
        ar = []
        if typ == 1:
            # ar = list(filter(lambda x: not int(x) % 2, lst))
            ar = [i for i in lst if i % 2 == 0]
        elif typ == 0:
            # ar = list(filter(lambda x: int(x) % 2, lst))
            sr = [i for i in lst if i % 2 != 0]
        return ar
    return m_lst


if __name__ == '__main__':
    mylist = list(map(int, input().split()))
    a = int(input("Введите:\n 0, если хотите удалить чётные\n 1, если хотите удалить нечётные\n"))
    print(mod_list(mylist)(a))
