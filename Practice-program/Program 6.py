while True:
    try:
        str1 = input("请输入需要计算的数学算式(输入'q'退出):")
        equation = eval(str1)
        if equation:
            print(equation)
        elif equation == 'q':
            print("退出计算器")
            break
        else:
            break
    except NameError:
        print("输入有误")
