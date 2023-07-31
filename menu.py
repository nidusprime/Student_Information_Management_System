"""
选择菜单
"""


def menu():
    print('=' * 50)
    print('-' * 20 + 'Student Information Management System' + '-' * 20)
    print(' ' * 10 + "1.录入学生信息")
    print(' ' * 10 + "2.查找学生信息")
    print(' ' * 10 + "3.删除学生信息")
    print(' ' * 10 + "4.修改学生信息")
    print(' ' * 10 + "5.排序")
    print(' ' * 10 + "6.统计学生总人数")
    print(' ' * 10 + "7.显示所有学生信息")
    print(' ' * 10 + "0.退出系统")
    print('-' * 77)
    s = input('请输入你要选择的操作:')
    return s
