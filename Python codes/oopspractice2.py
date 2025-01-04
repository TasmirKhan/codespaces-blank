print("This is a practice file for OOPs in Python")
class circle:
   
    def __init__(self, radius=2):
        self.radius = radius
        print("New circle created with radius:",radius)

    def area(self):
        print("Area of the circle is ", 3.14*self.radius*self.radius)
        return 3.14*self.radius*self.radius
    
    def perm(self):
        print("Perimeter of the circle is ", 2*3.14*self.radius)
        return 2*3.14*self.radius

c1 = circle(4)
# c1.area()
print(c1.area())
c1.perm()


print("\n\nNow we will create another class for practice")
class Employee:
    name = "Anonymous"
    age = "private"
    role = "Engineer"
    department ="Computer and AI"
    salary = "100000 Kuwaiti Dinar/month"
    def __init__(self, role = "Anonymous", department ="Unknown", salary = 0):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("Role: ", self.role)
        print("Department: ", self.department)
        print("Salary: ", self.salary)


e1 = Employee("Management", 230, "10 Millions Kuwaiti Dinar")
e1.showdetails()

print("\n\nNow we will create another Engineer class for practice")
class Engineer(Employee):
    def __init__(self):
        print("Engineer class created")
        super().__init__()




e2 = Engineer()
e2.showdetails()