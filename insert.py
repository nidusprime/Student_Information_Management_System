"""
录入学生信息的功能
"""


def insert():
    print("请根据提示输入学生信息 ")
    stu_list = []
    while True:
        stu_id = input('请输入学生学号(例如01)：')
        if not stu_id:
            break
        name = input('请输入学生姓名：')
        if not name:
            break
        try:
            math_grades = int(input('请输入学生数学成绩：'))
            chinese_grades = int(input('请输入学生语文成绩：'))
            english_grades = int(input('请输入学生英语成绩：'))
        except:
            print('输入数据无效请重新输入')
            continue
        stu = {'id': stu_id, 'name': name, 'math_grades': math_grades, 'chinese_grades': chinese_grades,
               'english_grades': english_grades}
        stu_list.append(stu)
        ans = input('是否继续添加学生信息?y/n')
        if ans == 'y' or ans == 'Y':
            continue
        else:
            break
    save(stu_list)
    print('学生信息录入完毕！！')


# save函数用于把列表的学生数据保存在文件中
def save(list1):
    try:
        stu = open('stu_infor.txt', 'a', encoding='UTF-8')
    except:
        stu = open('stu_infor.txt', 'w', encoding='UTF-8')
    for item in list1:
        stu.write(str(item) + '\n')
    stu.close()
