
# # manually create instance variable takes lot of time
# # emp_1.first = 'ellai'
# # emp_1.last = 'dhurai'

# # emp_2.first = 'ellai'
# # emp_2.last = 'dhurai'


# # create a instance variable using class method
# class Employee:

#     # __init__ is special constructor method it initialize the process constructing instance variable.
#     # when we create a method within a class they receive an instance/variable as first argument automatically.
#     # so we can assign the instance variable using self. we can change this name. our arguments should be passed after self.
  
#     # class variable
#     no_of_emp = 0
#     raise_amount = 1.4
    
#     # methods
#     # __init__ is a special method it initialize the class constructor
#     def __init__(self, first, last, pay):
#         # emp_1.first = 'ellai'
#         # self.fname = first => we can use variable like this.
#         self.first = first
#         self.last = last
#         self.email = first + last + '@gmail.com'
#         self.pay = pay

#         # if the value is constant we can use class variable to do an operation
#         Employee.no_of_emp += 1
        
#     # after creating instance variable we can use it in our class methods
#     def fullname(self):
#         return '{}{}'.format(self.first, self.last)

#     def apply_raise(self):
#         # with class object Employee.raise_amount also used to access class variable
#         # if we use a self.raise_amount instead of Employee.raise_amount we can change the instance value when we want.
#         self.pay = int(self.pay * self.raise_amount)

#     # Dunder method special class method
#     # __repr__ used for logging and debugging
#     def __repr__(self):
#         return "Employee('{}''{}','{}')".format(self.first,self.last,self.pay)
    
#     # __str__ used for readable representation of object
#     def __str__(self):
#         return '{}-{}'.format(self.fullname(),self.email)
        

            
# # create employee instance / variable
# emp_1 = Employee('ellai', 'dhurai', 5000)
# emp_2 = Employee('sundar', 'raj', 6000)

# print(repr(emp_1))  
# print(emp_1)  # ==> print(emp1.__str__())

# # to access the return value of emp_1 instance we need to use that function
# # print(emp_1.fullname())

# # the above is transformed like this when we run. here we need to pass instance as self in our method
# # print(Employee.fullname(emp_1))

# # emp_1.raise_amount = 1.05
# # print(emp_1.raise_amount)
# # print(Employee.no_of_emp)

# # inheriting properties from parent class (Employee) to sub class (Developer)
# class Developer(Employee):
#     # when use child to make changes anything in parent class does not affect.
#     raise_amount = 1.5

#     def __init__(self, first, last, pay, language):
#         self.language = language  # Developer class instance

#         super().__init__(first, last, pay)
#         # Employee.__init__(self, first,last,pay)
#         # super().__init__ method is used to pass child class instance to parent class


# # print(help(Developer)) # returns all inheritance properties

# dev_1 = Developer('ellai', 'dhurai', 5000, 'tamil')
# dev_2 = Developer('sundar', 'raj', 6000, 'english')

# # print(dev_1.language)
# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)


# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
        
#         if employees == None:
#                 self.employees = []
#         else:
#             self.employees = employees
        
#     def add_emp(self,emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
    
#     def remove_emp(self,emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
    
#     def list_emp(self):
#         for emp in self.employees:
#             print(emp.fullname())
            
# mgr_1 = Manager('ganesh','kumar',5000,[dev_1])

# print(mgr_1.email)

# # adding created employees in the Developer class to manager class
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# mgr_1.list_emp()

# # check manager is instance of parent class Employee
# print(isinstance(mgr_1, Employee))
# # check if manager is subclass of Employee
# print(issubclass(Manager, Employee))

# # class HTTPexception(Exception)


# # @property decorator in class method
# class Employees:
    
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
        
#     @property
#     # property decorator is used change the attribute value dynamically.
#     def email(self):
#         return '{}.{}@gmail.com'.format(self.first,self.last)
    
#     @property
#     def fullname(self):
#         return '{}{}'.format(self.first,self.last)
    
#     # setter is used to set the attribute value
#     # without this decorator we cant change attribute value
  
#     @fullname.setter
#     def fullname(self,name):
#         first,last = name.split(' ')
#         self.first = first
#         self.last = last
        
#     @fullname.deleter
#     def fullname(self):
#         print('Deleted!')
#         self.first = None
#         self.last = None
        

# emp_1 = Employees('ellai', 'dhurai')

# # here we can the attribute fullname.
# emp_1.fullname = 'Prem kumar'

# print(emp_1.email)
# print(emp_1.fullname)

# # del emp_1.fullname