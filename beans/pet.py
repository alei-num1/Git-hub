class Car:
    def __init__(self, car_type="", car_name=""):
        self.car_type = car_type
        self.car_name = car_name

    def car_move(self):
        print("%s %s is moving." % (self.car_type, self.car_name))

    def car_stop(self):
        print("%s %s  stopped." % (self.car_type, self.car_name))


# 创建实例
car1 = Car(car_type="宝马", car_name="X6")
car1.car_move()
car1.car_stop()
