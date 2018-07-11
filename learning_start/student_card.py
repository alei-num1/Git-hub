card_infors = []
import sys

# 打印功能提示
def print_menu():
    print("=" * 50)
    print("名片管理系统 v01")
    print("1 增加一个名片")
    print("2 修改一个名片 v01")
    print("3 查询一个名片 v01")
    print("4 删除一个名片 v01")
    print("5 显示所有的名片")
    print("6 退出系统 v01")


# 定义一个管理系统类
class Student_management:
    def __init__(self):
        self.student = Student()

    def add_stu_info(self, card_infors):
        stu_result = self.student.get_stu_info()
        new_infor = {}
        new_infor['name'] = stu_result.new_name
        new_infor['we_chat'] = stu_result.new_we_chat
        new_infor['qq'] = stu_result.new_qq
        new_infor['address'] = stu_result.new_address

        card_infors.append(new_infor)
        return card_infors

    def modify_stu(self):
        stu_id = int(input("请输入要修改的学生的序号："))
        self.student.get_stu_info()
        new_infor_2 = {}
        new_infor_2[stu_id - 1]['name'] = self.student.get_stu_info.new_name
        new_infor_2[stu_id - 1]['we_chat'] = self.student.get_stu_info.new_we_chat
        new_infor_2[stu_id - 1]['qq'] = self.student.get_stu_info.new_qq
        new_infor_2[stu_id - 1]['address'] = self.student.get_stu_info.new_address
        card_infors.append(new_infor_2)

    def find_stu(self):
        find_name = input("请输入要查找的名字:")
        find_flag = 0  # 默认表示没有找到
        for temp in card_infors:
            if find_name == temp["name"]:
                print("已经找到", temp["name"], temp["we_chat"], temp["qq"], temp["address"])
                find_flag = 1
                break
        if find_flag == 0:
            print("查无此人")

    def del_stu(self):
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

    def display_stu(self):
        print("name we_chat qq address")
        for temp in card_infors:
            print(temp["name"], temp["we_chat"], temp["qq"], temp["address"])

    def quit_system(self):
        sys.exit()


# 定义学生类
class Student:

    def get_stu_info(self):
        new_name = input("请输入新的名字:")
        new_we_chat = input("请输入新的微信:")
        new_qq = input("请输入新的QQ:")
        new_address = input("请输入新的地址:")
        return new_name, new_we_chat, new_qq, new_address


def main():
    print_menu()
    while True:
        num = int(input("请输入对应的操作序号:"))
        if num == 1:
            print(Student_management.add_stu_info(card_infors))
