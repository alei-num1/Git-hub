class Car_sore():
    def order(self, money):
        if money > 50000:
            return Car()

    pass


class Car():
    def move(self):
        print('车在移动')

    def music(self):
        print('正在播放音乐')

    def stop(self):
        print('车停了')

class Suo_na_ta(Car):
    pass
class Ming_tu(Car):
    pass

car_store = Car_sore()
car = car_store.order(100000)
car.move()
car.music()
car.stop()

