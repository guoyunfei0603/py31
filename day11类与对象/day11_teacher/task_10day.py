
import random
import os


def copy_file(path,path2):
    # 第一步：获取目标路径中所有的文件和目录
    try:
        file_list = os.listdir(path)
    except:
        print('传入的路径不正确')
    else:
        # 第二步：遍历文件，
        for item in file_list:
            # 拼接该文件的完整路径
            file_path = os.path.join(path, item)
            # 第三步：判断是不是文件，是的话就进行copy
            if os.path.isfile(file_path):
                # 打开文件，读取内容
                with open(file_path, 'rb') as f:
                    contnet = f.read()

                # 在当前目录创建副本文件，写入内容
                new_file = 'cp' + item
                new_file =os.path.join(path2,new_file)
                with open(new_file, 'wb') as f:
                    f.write(contnet)


# copy_file(r'C:\project\py31_class\py31_09day',r"C:\project\py31_class\copy009")


def work3():
    print('---石头剪刀布游戏开始----')
    print('请按下面提示出拳：')
    # 创建一个列表来存储 石头 剪刀 布
    li = ['石头', '剪刀', '布']

    while True:
        print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
        # 用户输入数字
        try:
            user_num = int(input('请输入你的选项：'))
        except:
            print('您出拳有误，请按规矩出拳')
            continue
        # 电脑随机生成数字
        r_num = random.randint(1, 3)
        if 1 <= user_num <= 3:
            # 判断用户和电脑是否相等
            if r_num == user_num:
                print('您的出拳为:{}，电脑出拳:{}，平局'.format(li[user_num - 1], li[r_num - 1]))
            # 判断用户胜利的情况
            elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
                print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(li[user_num - 1], li[r_num - 1]))
            else:
                print('您的出拳为:{}，电脑出拳:{}，您输了'.format(li[user_num - 1], li[r_num - 1]))
        # 用户输入4，游戏结束
        elif user_num == 4:
            print('游戏结束')
            break
        else:
            print('您出拳有误，请按规矩出拳')

work3()
