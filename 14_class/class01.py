# pass 는 파이썬에서 아무 작업도 수행하지 않는 빈 코드 블록을 만들 때 사용
# 문법적으로 특정 블록이 필요하지만, 실제로 수행할 작업이 없을 때 사용
# while True:
#     pass
# class Car:
#     pass

class Car:
    def __init__(self, model, price): #생성자, 객체가 생성될 때 자동으로 실행
        # self는 현재 생성되는 객체 자신을 의미
        self.model = model
        self.price = price
        print(f"모델 이름:{self.model},가격:{self.price} 객체 생성!")

    def __del__(self): # 소멸자, 객체가 메모리에서 삭제될 때 자동으로 호출
        print(f"{self.model}의 객체가 소멸됨!")

    def drive(self, speed, distance): # speed, distance는 외부에서 전달받는 매개변수
        # self는 이 메서드를 호출하는 객체 자기 자신을 참조
        print(f"{self.model}가 {speed}km/h 속도로 {distance}km 만큼 전진")

car1 =Car("avante","2400") # Car 클래스에 대한 인스턴스
car2 =Car("santafe","4300")

print(car1.price) # 해당 객체의 속성에 접근 가능
print(car2.model)

car1.drive(80, 5)
car2.drive(100,10)

# 임의로 객체를 소멸시키는 법
del car2 # 이 시점에서 car2 소멸된다! (종료시점이 아니라)

Car.drive(car1,120,15)
# 클래스를 통해 직접 메서드를 호출, 이 경우 첫번재 인자로 객체자신을 명시적으로 전달