#self module is like initializing an function within itself, so whenever that function will be called in script, that function will print same result everytime.

#below is the class with two attributes company & salary, mention company as 'disco company' but for salary attrobute define a function

class employee:
    compamny = "disco company"
    def getsalary(self):
        print("Salary is 500 NOKS")

jacky = employee()     #onboarding jacky into the class

jacky.getsalary()    #now you are calling the above function 'getsalary', remember it's a 'self' function, you dont even need print command                     here, function will just write what you mentioned in it...no matter whereever the function is called 


