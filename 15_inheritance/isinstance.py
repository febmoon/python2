# from symtable import Class
#
# from inheritance import Animal,Dog
#
# dog1 = Dog("방울이")
# ##isinstance(객체, 클래스) : 객체가 해당클래스 또는 부모클래스의 인스턴스인지 확인
# print(isinstance(dog1,Dog)) # True
# print(isinstance(dog1,Animal)) #True
#
# animal1 = Animal("일반동물")
# print(isinstance(animal1,Dog)) # False
# print(isinstance(animal1, Animal)) #True

# person, student, teacher 3개의 클래스를 만들고
class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade
class Teacher(Person):
    def __init__(self,name, subject):
        super().__init__(name)
        self.subject = subject

def who(obj):
    if isinstance(obj,Student) :
        print(f"{obj.grade}학년 학생 {obj.name}입니다.")
    elif isinstance(obj,Teacher):
        print(f"{obj.subject}담당 {obj.name} 선생님입니다.")
    elif isinstance(obj,Person):
        print(f"일반시민 {obj.name}입니다.")
    else:
        print("알 수 없는 타입의 객체입니다")

person1 = Person("수진")
student1 = Student("조수진",6)
teacher1 = Teacher("이동윤","파이썬")
str1="anc"
who(person1) #일반시민 수진입니다.
who(student1)#6학년 학생 조수진입니다.
who(teacher1) #파이썬담당 이동윤 선생님입니다.
who(str1) #알 수 없는 타입의 객체입니다


