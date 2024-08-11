# 문제
# 주차장을 위한 시스템을 만들어야 함
# 주차장은 big, medium, small 타입의 공간이 있음 (공간의 개수가 함께 주어짐)
# 정수 carType 은 3일 경우 small, 2라면 medium, 1이라면 big 에 주차 가능
# 주차가 불가능하면 False를 반환

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)