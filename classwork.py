class human:
    attr1="human"
    attr2="student"
    def fun(self):
        print("i am a",self.attr1)
        print("i am a",self.attr2)
rodger = human()
print(rodger.attr1)
rodger.fun()
#*************************************
class Python:
	def __init__(self, name, company):
		self.name = name
		self.company = company
	def show(self):
		print("Hello my name is " + self.name+" and I" +
			" work in "+self.company+".")
obj = Python("Ghufran", "Bano Qabil")
obj.show()
#*****************************
# define a class
class Employee:
    # define an attribute
    employee_id = 0
# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()
# access attributes using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")
# access attributes using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}") 
#********************************************
class room:
    length=0.0
    bredth=0.0
    def calculate_area(self):
        print("area of room=",self.length*self.breadth)
study_room = room()
study_room.length=42.5
study_room.breadth=30.8
study_room.calculate_area()
#*****************************
class Employee:
    __id=0
    __name=""
    __gender=""
    __city=""
    __salary=0
    def setData(self):
        self.__id=int(input("Enter Id:\t"))
        self.__name = input("Enter Name:\t")
        self.__gender = input("Enter Gender:\t")
        self.__city = input("Enter City:\t")
        self.__salary = int(input("Enter Salary:\t"))
    def showData(self):
        print("Id\t\t:",self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)


def main():
    #Employee Object
    emp=Employee()
    emp.setData()
    emp.showData()

if __name__=="__main__":
    main()

        

















