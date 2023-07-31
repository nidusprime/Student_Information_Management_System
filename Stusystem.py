"""
简单的学生信息管理系统
"""
import os
import re
import menu
import sys
import insert
import search
import delete
import modify
import sort
import total
import show

while True:
    s = menu.menu()
    if s in ['0', '1', '2', '3', '4', '5', '6', '7']:
        if s == '1':
            insert.insert()
        elif s == '2':
            search.search()
        elif s == '3':
            delete.delete()
        elif s == '4':
            modify.modify()
        elif s == '5':
            sort.sort()
        elif s == '6':
            total.total()
        elif s == '7':
            show.show()
        elif s == '0':
            answer = input('您确定要退出系统吗？y/n:')
            if answer == 'y' or answer == 'Y':
                print('感谢您的使用')
                sys.exit()
            else:
                continue
    else:
        print('请输入0-7，而不是瞎几把输😓')
