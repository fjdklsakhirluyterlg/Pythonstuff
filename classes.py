class Parent:
    BloodGroup = 'A'
    Gender = 'Male'
    Hobby = 'Chess'
    
# creating child class
class Child(Parent): # inheriting parent class
    BloodGroup = 'A+'
    Hobby = "Airplanes"
    
    def print_data(Child):
        print(Child.BloodGroup, Child.Gender, Child.Hobby)
    
# creating object for child class
child1 = Child()
child1.Hobby = "Horses"
child2 = Child()
child2.BloodGroup = "O"
# as child1 inherits it's parent's hobby printed data would be it's parent's
child1.print_data()
child2.print_data()