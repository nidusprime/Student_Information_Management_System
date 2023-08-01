"""
统计学生信息
"""
import os.path


def total():
    lab = 0
    if os.path.exists('stu_infor.txt'):
        with open('stu_infor.txt', 'r', encoding='utf-8') as file:
            stu_file = file.readlines()
        for item in stu_file:
            lab += 1
        print('一共查询到{0}个人，查询结束！'.format(lab))
    else:
        print('暂时未查询到学生信息库')
