# This code will show you how to define function with 'property' method, so that you acn re-use the formula again & again

class employee:
    company = "abc"
    salary = 5000
    bonus = 4000
    #totalsalary = 9000 #instead of hardcoding totalsalary, use 'property' function

    @property
    def totalsalary(self):
        return self.salary + self.bonus

e = employee()
print(e.totalsalary)

e.salary = 2000
e.bonus = 3000

print(e.totalsalary)
