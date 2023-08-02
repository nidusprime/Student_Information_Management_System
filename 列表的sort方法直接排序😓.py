import search

with open('stu_infor.txt', 'r', encoding='utf-8') as rfile:
    stu_file = rfile.readlines()

stu_list = []
for i in stu_file:
    stu_list.append(eval(i))
print(stu_list)

search.show_gui()
stu_list.sort(key=lambda stu_dic: int(stu_dic['english_grades']), reverse=True)
for item in stu_list:
    print(item)
