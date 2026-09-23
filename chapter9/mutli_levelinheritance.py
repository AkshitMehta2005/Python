class Employee:
    company = "ITC"

    def showEmployee(self):
        print("This is an Employee")


class Programmer(Employee):
    language = "Python"

    def showProgrammer(self):
        print("This is a Programmer")
        print(f"Language: {self.language}")


class Developer(Programmer):
    framework = "Django"

    def showDeveloper(self):
        print("This is a Developer")
        print(f"Framework: {self.framework}")


d = Developer()

d.showEmployee()
d.showProgrammer()
d.showDeveloper()