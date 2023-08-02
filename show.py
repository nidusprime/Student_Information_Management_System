"""
显示学生全部信息
"""
import os.path

import search


def show():
    if os.path.exists('stu_infor.txt'):
        search.show_gui()
        stu_info_list = []
        with open('stu_infor.txt', 'r', encoding='utf-8') as file:
            stu_list = file.readlines()
        if len(stu_list) == 0:
            print('现在还没存储任何学生信息哦！')
        for item in stu_list:
            stu_info_list.append(eval(item))
        show_stu(stu_info_list)
    else:
        print('暂时没有查询到学生信息库！')


def show_stu(list1):
    for ite in list1:
        print(
            '\t' + ite['id'] + '\t\t' + ite['name'] + '\t\t\t\t' + str(ite['math_grades']) + '\t\t\t\t' +
            str(ite['chinese_grades']) + '\t\t\t\t\t' + str(ite['english_grades']) + '\t\t\t\t' +
            str(ite['math_grades'] + ite['chinese_grades'] + ite['english_grades']))
