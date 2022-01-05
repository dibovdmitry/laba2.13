#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def commands():
    print("Список команд:\n")
    print("add - добавить маршрут;")
    print("list - вывести список маршрутов;")
    print("select - найти самолёты по номеру")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def get_race(races):
    path = input("Пункт назначения ")
    number = input("Номер самолёта ")
    model = float(input("Тип самолёта "))

    race = {
        'path': path,
        'number': number,
        'model': model,
    }
    races.append(race)
    if len(races) > 1:
        races.sort(key=lambda item: item.get('race', ''))


def display_races(way):
    if way:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 4,
            '-' * 20
        )
        print(line)
        print(
            '| {:^30} | {:^4} | {:^20} |'.format(
                "Пункт назначения",
                "Номер самолёта",
                "Тип самолёта"
            )
        )
        print(line)

        for race in way:
            print(
                '| {:<30} | {:>4} | {:<20} |'.format(
                    race.get('path', ''),
                    race.get('number', ''),
                    race.get('model', '')
                )
            )
        print(line)

    else:
        print("Рейсы не найдены")


def select_races(way, parts, sel):
    result = []
    parts = way.split(' ', maxsplit=2)
    sel = str(parts[1])

    for race in way:

        if race <= sel:
            result.append(race)

    return result
