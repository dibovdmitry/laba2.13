#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from folder import commands, get_race, display_races, select_races


if __name__ == '__main__':
    races = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            get_race(races)

        elif command == 'list':
            display_races(races)

        elif command == 'select':
            race_select = input().split()
            selected = select_races(races, race_select)
            display_races(selected)

        elif command == 'help':
            commands()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
