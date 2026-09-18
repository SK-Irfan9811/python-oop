class Student:

    college="Stark University" #class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    #instance method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    #class method
    @classmethod
    def display_college_info(cls):
        print(f"College: {cls.college} {cls}")

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

s1=Student("Irfan", 24)
s2=Student("Mahira khan", 30)
s3=Student("Spider man", 26)

# print(Student.__dict__)
# print(s1.__dict__, s2.__dict__, s3.__dict__)

s1.display_college_info()
# Student.display_college_info(s1)

Student.display_info(s2)