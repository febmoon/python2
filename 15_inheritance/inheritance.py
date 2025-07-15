# 부모 클래스(Super Class)
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 동물 객체 생성!")
    def speak(self):
        print(f"{self.name}이(가) 소리를 냅니다.")
    def move(self):
        print(f"{self.name}이(가) 움직입니다.")

# ------------- 상속 시작 -------------
# 자식클래스(Subb Class)
# 괄호 안에 부모 클래스 이름을 명시해서 상속 선5

class Dog(Animal):
    def wag(self):
        print(f"{self.name}이(가) 꼬리를 흔듭니다.")
    def speak(self): # method overriding!! 부모클래스의 speak 메서드를 재정의(Overriding)
        print("왈왈")

class Cat(Animal):
    def speak(self):
        print("애옹") # method overridin
    def climb(self):
        print(f"{self.name}이(가) 높은 곳에 올라갑니다.")
animal1 = Animal("일반동물")
animal1.move()
animal1.speak()

dog1 = Dog("방울이")
dog1.move()
dog1.speak()
dog1.wag()

cat1 = Cat("냐옹이")
cat1.climb()
cat1.move()
cat1.speak()
'''
메서드 오버라이딩(재정의) : 같은 이름의 메서드를 자식클래스에서 다시 정의하여 동작변경
'''

# Shape라는 부모클래스 -> color
# 메서드 describe-> 이 도형의 색깔은 입니다. 출력

# Circle 자식 클래스 ->
# 메서드 describe 오버라이딩 -> 이 원의 색깔은 입니다. 출력
# 메서드 get_area(radius)-> math.pi모듈 이용해서 넓이 구해서 리턴
# 리턴한 것을 print로 출력할 때 (소수점 둘째까지)
import math
class Shape:
    def __init__(self,color):
        self.color = color
    def describe(self):
        print(f"이 도형의 색깔은 {self.color}입니다.")
class Circle(Shape):
    def describe(self):
        print(f"이 원의 색깔은 {self.color}입니다.")
    def get_area(self, radius):
        return math.pi*(radius**2) # 제곱은 별 2개!!

shape1 = Shape("red")
shape1.describe()

circle1 = Circle("blue")
circle1.describe()
print(f"원의 넓이 : {circle1.get_area(5):.2f}") # 소수점 둘째자리까지 나타내기 :.2f

