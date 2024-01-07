#just initiating a simple class statement with two variables/attributes - employee & salary
class company:
    employee = "engineers"
    salary = 1000

jacky = company()              #onboarding jacky into the company

print(jacky.salary)            #this print command will just print the salary of jacky, remember salary is hardcoded above as 1000


#now lets change the salary & hardcode jacky salary  it to different value

jacky.salary = 5000

#print jacky salary again, now it will give result as 5000

print(jacky.salary)





