"""
查找学生信息功能
"""


def search():
    while True:
        lab = 0
        sel = input('若想根据id查询输入1，若想更具姓名查询输入2：')
        if sel == '1':
            stu_id = input('请输入所要查询学生的id：')
            with open('stu_infor.txt', 'r', encoding='utf-8') as file:
                file_list = file.readlines()
            for item in file_list:
                if stu_id in item:
                    lab += 1
                    show_gui()
                    ite = eval(item)
                    print(
                        '\t' + ite['id'] + '\t\t' + ite['name'] + '\t\t\t\t' + str(ite['math_grades']) + '\t\t\t\t' +
                        str(ite['chinese_grades']) + '\t\t\t\t\t' + str(ite['english_grades']))
            if lab == 0:
                print('没有查询到id为{0}的学生'.format(stu_id))
        elif sel == '2':
            stu_name = input('请输入所要查询学生的姓名：')
            with open('stu_infor.txt', 'r', encoding='utf-8') as file1:
                file1_list = file1.readlines()
                for item in file1_list:
                    if stu_name in item:
                        lab += 1
                        ite = eval(item)
                        show_gui()
                        print('\t' + ite['id'] + '\t\t' + ite['name'] + '\t\t\t\t' + str(ite['math_grades'])
                              + '\t\t\t\t' + str(ite['chinese_grades']) + '\t\t\t\t\t' + str(ite['english_grades']))
                if lab == 0:
                    print(f"没有查询到姓名为:{stu_name}的学生")
        else:
            print('请输入1或者2！！！！')
            continue
        answer = input('是否要继续查询学生信息？y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            print('查询信息结束！')
            break


def show_gui():
    print(
        '\t' + 'ID' + '\t\t' + 'Name' + '\t\t' + 'Math_grades' + '\t\t' + 'Chinese_grades' + '\t\t' + 'English_grades')
