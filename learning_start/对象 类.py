class Dog:
    # 属性
    # 方法
    def eat(self):
        print("It is eating bones...")

    def drink(self):
        print("It is drinking water...")

    def introduce(self):
        print("%s的年龄是:%d" % ())


# 创建一个对象
tom = Dog()
# 调用tom指向对象的方法
tom.eat()
tom.drink()
# 给tom的对象添加2个属性
tom.name = "汤姆"
tom.age = 13

tom.introduce()
