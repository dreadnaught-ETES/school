class Person:
    def __init__(self, first=' ', last=' ', job=' ', age=' '):
        self.first_name_str=first
        self.last_name_str=last
        self.job_str=job
        self.age_int=age
    def __str__(self):
        return "My name is {} {}, my job is {} and I am {} years old.".format\
            (self.first_name_str,self.last_name_str, self.job_str, self.age_int)