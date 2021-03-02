class Person:
    def __init__(self, first=' ', last=' ', job=' ', age=' '):
        self.first_name_str=first
        self.last_name_str=last
        self.job_str=job
        self.age_int=age
    def __str__(self):
        return "My name is {} {}, my job is {} and I am {} years old.".format\
            (self.first_name_str,self.last_name_str, self.job_str, self.age_int)
#above is one class definition to be used for people
class Animal:
    def __init__(self, name=' ', owner=' ', species=' '):
        self.name_str=name
        self.owner_str=owner
        self.species_str=species
    def __str__(self):
        return "This is {}, they are {}'s {}.".format\
            (self.name_str, self.owner_str, self.species_str)
#then we have a secondary class to be used for pets of those people.
P1 = Person(first='Elion', last='Masters', job='Quantum Physicist', age='31')
A1 = Animal(name='Floof', owner='Elion', species='Norwegian Forest Cat')
#here we have made 2 different instances for both People and Animal Class objects.
P2 = Person(first='Willow', last='Starling', job='Barista', age='29')
A2 = Animal(name='Meeko', owner='Willow', species='Maine Coon Mix')
print(P1)
print(A1)
print(P2)
print(A2)
P2.last_name_str='Masters'
#now we have changed P2's last name as if they married P1
print(P2)
#one of the best things about this is we can add all sorts of attributes. we can teach the animals tricks or skills by adding a list in the class definition.