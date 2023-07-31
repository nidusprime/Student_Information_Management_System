"""
修改学生信息
"""
import insert


def modify():
    mod_stu_dic = {}
    mod_stu_list = []
    lab = 0
    while True:
        stu_id = input('请输入所要修改学生的id：')
        with open('stu_infor.txt', 'r', encoding='utf-8') as file:
            file_list = file.readlines()
        with open('stu_infor.txt', 'w', encoding='utf-8') as file1:
            for item in file_list:
                if stu_id not in item:
                    file1.write(str(item))
                else:
                    print('已找到学生请按下列提示进行修改')
                    lab += 1
                    name = input('请修改学生姓名：')
                    if not name:
                        break
                    try:
                        math_grades = int(input('请修改学生数学成绩：'))
                        chinese_grades = int(input('请修改学生语文成绩：'))
                        english_grades = int(input('请修改学生英语成绩：'))
                    except:
                        print('输入数据无效请重新输入')
                        continue
        if lab == 0:
            print('没有找到该学号的学生！')
            break
        else:
            mod_stu_dic = {'id': stu_id, 'name': name, 'math_grades': math_grades,
                           'chinese_grades': chinese_grades,
                           'english_grades': english_grades}
            mod_stu_list.append(mod_stu_dic)
            print('信息修改完毕！')
        answer = input('是否要继续修改学生信息？y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            insert.save(mod_stu_list)
            break
