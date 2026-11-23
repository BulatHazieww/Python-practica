class Student:
    tel_number = "+7-937-289-12-05"

    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades


    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.grades.append(grade)
            print(f"Оценка {grade} добавлена студенту {self.name}")
        else:
            print("Ошибка! Оценка должна быть от 1 до 5.")


    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


    def info(self):
        print( )
        print("Имя:", self.name)
        print("Группа:",self.group)
        print("Оценки:", self.grades)
        print("Средний балл:", round(self.get_average(), 2))
        print("Номер телефона:", self.tel_number)
        print( )



student1 = Student("Анна", "36-64", [5, 4, 3, 5])
student2 = Student("Иван", "36-64", [4, 4, 5, 3])
student3 = Student("Сергей", "36-63", [3, 5, 4, 5])


student1.add_grade(3)
student2.add_grade(4)
student3.add_grade(2)


student1.info()
student2.info()
student3.info()