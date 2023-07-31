"""
删除学生信息
"""


def delete():
    while True:
        lab = 0
        stu_id = input('请输入要删除学生的学号：')
        file = open('stu_infor.txt', 'r', encoding='utf-8')
        file_list = file.readlines()
        file1 = open('stu_infor.txt', 'w', encoding='utf-8')
        for item in file_list:
            if stu_id not in item:
                file1.write(str(item))
            else:
                lab += 1
        if lab == 0:
            print("没有找到该学号的学生！")
        else:
            print('学号为' + stu_id + '的学生已经被删除')
        answer = input("是否继续进行删除？y/n")
        if answer == 'y' or answer == 'Y':
            file.close()
            file1.close()
            continue
        else:
            break
