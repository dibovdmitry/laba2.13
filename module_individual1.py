#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def string():
    def sophia():
        a = list(map(int, input("Напишите строки через пробел: ").split()))
        print("<ol>\n")

        for i in a:
            print(f"<li> строка {i}</li>\n")

        print("</ol>")
    return sophia()
