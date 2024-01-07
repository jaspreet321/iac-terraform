class techcompany:
   engineer = "techie"
   junior = "junior techie"
   salary_engineer = "5000NOK"  # I am taking salary in " ", because I am also writing NOK with digits, so it has to be considered as string
   salary_junior = "2000NOK"


employee1 = techcompany()
employee2 = techcompany()


print("employee1 is a " + employee1.engineer)
print("emplloyee2 is a " + employee2.junior)
print("employee1 salary is " + employee1.salary_engineer)
print("employee2 salary is " + employee2.salary_junior)


