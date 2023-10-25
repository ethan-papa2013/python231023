class Person:
    def __init__(self, id, phoneNumber):
        self.id = id
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print(f"ID: {self.id}")  # ID 출력
        print(f"전화번호: {self.phoneNumber}")  # 전화번호 출력


class Manager(Person):
    def __init__(self, id, phoneNumber, skill):
        super().__init__(id, phoneNumber)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"기술: {self.skill}")  # 기술 출력


class Employee(Manager):
    def __init__(self, id, phoneNumber, skill, department):
        super().__init__(id, phoneNumber, skill)
        self.department = department

    def printInfo(self):
        super().printInfo()
        print(f"부서: {self.department}")  # 부서 출력


# 예제 사용
person1 = Person("12345", "555-555-5555")
person1.printInfo()

print("")

manager1 = Manager("54321", "555-123-4567", "프로젝트 관리")
manager1.printInfo()

print("")

employee1 = Employee("98765", "555-987-6543", "소프트웨어 개발", "IT")
employee1.printInfo()