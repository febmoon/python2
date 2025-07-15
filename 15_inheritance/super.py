class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        print(f"차량 ({self.brand},{self.year}년식)이 생성되었습니다.")
    def display_info(self):
        print(f"브랜드: {self.brand}, 연식: {self.year}년식")

class Car(Vehicle):
    def __init__(self, brand, year, color):
        # super()를 사용하여 부모클래스 Vehicle의 __init__(생성자)를 호출
        # 이렇게 하면 brand, year의 속성이 vehicle 클래스의 생성자에서 초기화
        super().__init__(brand,year)
        self.color = color # car 클래스만의 새로운 속성 color를 초기화
        print(f"자동차 ({self.brand}, {self.year}년식, {self.color})가 생성되었습니다.")
    def display_info(self):
        # print(f"브랜드: {self.brand}, 연식: {self.year}년식, 색상:self.color}") 이렇게도 가능하지만
        # super()를 사용하여 부모클래스의 display_info메서드를 호출하고
        # 추가적으로 Car 클래스만의 정보인 색상을 출력
        super().display_info()
        print(f"색상: {self.color}")
    def drive(self):
        print(f"{self.color} {self.brand}가 운전 중입니다")
# 오토바이 클래스
# 생성자는 brand, year, type
# wheelie 메서드 -> 브랜드 색상 오토바이가 윌리를 합니다! 출력
class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type
        print(f"오토바이 ({self.brand}, {self.year}년식, {self.type})가 생성되었습니다.")
    def wheelie(self):
        print(f"{self.brand} {self.year} 오토바이가 윌리를 합니다!")

car1 = Car("Hyundai", 2025, "black")
car1.display_info()
car1.drive()

motorcycle1 = Motorcycle("Harley-Davidson", 2022, "Cruiser")
motorcycle1.wheelie()
motorcycle1.display_info()

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    def display_info(self):
        print(f"이름 : {self.name}, 사원 ID :{self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
    def display_info(self):
        super().display_info()
        print(f"부서 : {self.department}")
    def assign_task(self,task):
        print(f"{self.name} 매니저가 {task}를(을) 할당합니다.")

# 상속받아서 class manager
employee1 = Employee("sujin","CSJ")
employee1.display_info()

manager1 = Manager("heejune", "MHJ", "개발팀")
manager1.display_info()
manager1.assign_task("새로운 프로젝트 착수")

# git status
# git add .
# git commi -m "inheritance
# git push origin main
