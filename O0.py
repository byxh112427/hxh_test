import os
import shutil

dir_name = "E:\\20尺单箱\\"

file_list = os.listdir(dir_name)
# 获取按照文件时间创建排序的列表，默认是按时间升序
new_file_list = sorted(file_list, key=lambda file: os.path.getctime(os.path.join(dir_name, file)))
tmp = new_file_list.copy()

for i in tmp:
    new_dir = os.path.join(dir_name, i)
    new_list = os.listdir(new_dir)
    if len(new_list) == 5:
        print(new_list[0][4:-4])
        os.rename(new_dir, dir_name + '\\' + new_list[0][4:-4])




# des_name = "E:\\40尺单箱\\无效"
# for i in tmp:
#     new_dir = os.path.join(dir_name, i)
#     new_list = os.listdir(new_dir)
#     print(new_list)
#     #os.rename(new_dir,)






# if not os.path.isdir(dir_name + '有效'):
#     os.mkdir(dir_name + '有效')
#
# if not os.path.isdir(dir_name + '无效'):
#     os.mkdir(dir_name + '无效')
#
# j = 0
# for i in tmp:
#     j += 1
#     if j <= 0:
#         t = i[:4] + "TBJU08119762NUA.mp4"
#         os.rename(dir_name + i, dir_name + t)
#         shutil.move(dir_name + t, dir_name + '有效\\' + t)
#     else:
#         shutil.move(dir_name + i, dir_name + '无效\\' + i)
#     print("success")
