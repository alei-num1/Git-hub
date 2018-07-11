# [{"name": "老张", "age": "28"}, {"name": "老赵", "age": "25"}]
# 打印功能提示
print("=" * 50)
print("名片管理系统 v01")
print("1 增加一个名片")
print("2 删除一个名片 v01")
print("3 修改一个名片 v01")
print("4 查询一个名片 v01")
print("5 显示所有的名片")
print("6 退出系统 v01")
print("=" * 50)
# 用来存储名片
card_infors = []
while True:
    # 获取用户的输入
    num = int(input("请输入对应的操作序号:"))
    # 根据用户的数据执行相应的功能

    if num == 1:
        new_name = input("请输入新的名字:")
        new_we_chat = input("请输入新的微信:")
        new_qq = input("请输入新的QQ:")
        new_address = input("请输入新的地址:")

        # 定义一字典，用来存储一个新的名片
        new_infor = {}
        new_infor['name'] = new_name
        new_infor['we_chat'] = new_we_chat
        new_infor['qq'] = new_qq
        new_infor['address'] = new_address

        # 将一个字典添加到到列表中
        card_infors.append(new_infor)
        print(card_infors)

    elif num == 2:
        find_name = input("请输入要删除的名字:")
        symbol = 0  # 没有此人
        for temp in card_infors:
            if find_name == temp["name"]:
                del (temp["name"], temp["we_chat"], temp["qq"], temp["address"])
                print("已经删除")
            symbol = 1
            print(card_infors)
            break
        if symbol == 0:
            print("已经不存在")

    elif num == 3:
        find_name_2 = input("请输入要修改的名字:")
        mark = 0
        for temp2 in card_infors:
            if find_name_2 == temp2["name"]:
                # del (temp2["name"], temp2["we_chat"], temp2["qq"], temp2["address"])
                new_name2 = input("请输入新的名字:")
                new_we_chat2 = input("请输入新的微信:")
                new_qq2 = input("请输入新的QQ:")
                new_address2 = input("请输入新的地址:")

                # 定义一字典，用来存储一个新的名片
                new_infor_2 = {}
                new_infor_2['name'] = new_name2
                new_infor_2['we_chat'] = new_we_chat2
                new_infor_2['qq'] = new_qq2
                new_infor_2['address'] = new_address2

                temp = new_infor_2
                mark = 1
                print(card_infors)
                break

        if mark == 0:
            print("输入有误")

    elif num == 4:
        find_name = input("请输入要查找的名字:")
        find_flag = 0  # 默认表示没有找到
        for temp in card_infors:
            if find_name == temp["name"]:
                print("已经找到", temp["name"], temp["we_chat"], temp["qq"], temp["address"])
                find_flag = 1
                break
        if find_flag == 0:
            print("查无此人")

    elif num == 5:
        print("name we_chat qq address")
        for temp in card_infors:
            print(temp["name"], temp["we_chat"], temp["qq"], temp["address"])

    elif num == 6:
        break
    else:
        print("输入有误，请重新输入")
    # print(card_infors)
    print("")
