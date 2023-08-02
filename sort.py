"""
根据某个信息对学生进行排序
"""
import os.path

import search
import show


def sort():
    if os.path.exists('stu_infor.txt'):
        while True:
            stu_lst = []
            with open('stu_infor.txt', 'r', encoding='utf-8') as rfile:
                stu_file = rfile.readlines()
            for i in stu_file:
                stu_lst.append(eval(i))
            print('1.math_grades')
            print('2.chinese_grades')
            print('3.english_grades')
            print('4.all_grades')
            sel = input('请选择要根据哪门科目进行排序：')
            sel_ud = input('请选择升序还是降序? 1·升序 2·降序:')
            if sel_ud == '1':
                if sel == '1' or sel == '2' or sel == '3' or sel == '4':
                    if sel == '1':
                        sort_list = up_sor(stu_lst, 'math_grades')
                        search.show_gui()
                        show.show_stu(sort_list)
                        print("排序完成！")
                    elif sel == '2':
                        sort_list = up_sor(stu_lst, 'chinese_grades')
                        search.show_gui()
                        show.show_stu(sort_list)
                        print("排序完成！")
                    elif sel == '3':
                        sort_list = up_sor(stu_lst, 'english_grades')
                        search.show_gui()
                        show.show_stu(sort_list)
                        print("排序完成！")
                    else:
                        sort_list = up_all_sor(stu_lst)
                        search.show_gui()
                        show.show_stu(sort_list)
                        print("排序完成！")
                else:
                    print('输入1-4！输入有误')
                    continue
            else:
                if sel == '1' or sel == '2' or sel == '3' or sel == '4':
                    if sel == '1':
                        sort_list = down_sor(stu_lst, 'math_grades')
                        search.show_gui()
                        show.show_stu(sort_list)
                        print("排序完成！")
                    elif sel == '2':
                        sort_list = down_sor(stu_lst, 'chinese_grades')
                        search.show_gui()
                        show.show_stu(sort_list)
                        print("排序完成！")
                    elif sel == '3':
                        sort_list = down_sor(stu_lst, 'english_grades')
                        search.show_gui()
                        show.show_stu(sort_list)
                        print("排序完成！")
                    else:
                        sort_list = down_all_sor(stu_lst)
                        search.show_gui()
                        show.show_stu(sort_list)
                        print("排序完成！")
                else:
                    print('输入1-4！输入有误')
                    continue
            answer = input('是否要继续进行排序？y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                print('排序结束！')
                break
    else:
        print('学生信息库暂时还未建立')


def up_sor(list1, subjects):
    for i in range(1, len(list1)):
        for j in range(0, len(list1) - i):
            if list1[j][subjects] <= list1[j + 1][subjects]:
                continue
            else:
                list_va = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = list_va
    return list1


def down_sor(list1, subjects):
    for i in range(1, len(list1)):
        for j in range(0, len(list1) - i):
            if list1[j][subjects] >= list1[j + 1][subjects]:
                continue
            else:
                list_va = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = list_va
    return list1


def up_all_sor(lis):
    for i in range(1, len(lis)):
        for j in range(0, len(lis) - 1):
            if lis[j]['math_grades'] + lis[j]['chinese_grades'] + lis[j]['english_grades'] <= \
                    lis[j + 1]['math_grades'] + lis[j + 1]['chinese_grades'] + lis[j + 1]['english_grades']:
                continue
            else:
                list_va = lis[j]
                lis[j] = lis[j + 1]
                lis[j + 1] = list_va
    return lis


def down_all_sor(lis):
    for i in range(1, len(lis)):
        for j in range(0, len(lis) - 1):
            if lis[j]['math_grades'] + lis[j]['chinese_grades'] + lis[j]['english_grades'] >= \
                    lis[j + 1]['math_grades'] + lis[j + 1]['chinese_grades'] + lis[j + 1]['english_grades']:
                continue
            else:
                list_va = lis[j]
                lis[j] = lis[j + 1]
                lis[j + 1] = list_va
    return lis
