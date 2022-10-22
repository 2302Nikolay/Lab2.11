#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def f1():
    def f2(x):
        return x + 3
    return f2


if __name__ == '__main__':
    k = int(input())
    cnt = f1()
    print(cnt(k))
