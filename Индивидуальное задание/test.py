def mod_list(lst):
    def m_lst(typ):
        if typ == 1:
            return list(filter(lambda x: (x % 2) > 0, lst))
        elif typ == 0:
            return list(filter(lambda x: (x % 2) < 0, lst))
    return m_lst


mylist = list(map(int, input().split()))
a = int(input("Введите:\n 0, если хотите удалить чётные\n 1, если хотите удалить нечётные\n"))
print(mod_list(mylist)(a))
