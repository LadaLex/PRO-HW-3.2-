class  Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}"

class Student(Human):
    def __init__(self, name, surname, age, sex, nationality):
        super().__init__(name, surname, age)
        self.sex = sex
        self.nationality = nationality
    def __str__(self):
        return f"{super().__str__()}, {self.sex}, {self.nationality}"


class Group:
    def __init__(self):
        self.group_list = []

    def add_to_group(self, student):
        self.group_list.append(student)

    def remove_from_group(self, student):
        self.group_list.remove(student)

    def find_student(self, surname):
        for student in self.group_list:
            if student.surname == surname:
                return student

class CheckGroup(Exception):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit
    def __str__(self):
        return f"Sorry, group can't have more than {self.limit} students."
