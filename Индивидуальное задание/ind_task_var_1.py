def mod_list(lst):
    def m_lst(typ):
        if typ == 1:
            for i in lst:
                if i % 2 > 0:
                    lst.remove(i)
        elif typ == 0:
            for i in lst:
                if i % 2 == 0:
                    lst.remove(i)
        return lst
    return m_lst


mylist = list(map(int, input().split()))
a = int(input("Введите:\n 0, если хотите удалить чётные\n 1, если хотите удалить нечётные\n"))
print(mod_list(mylist)(a))
