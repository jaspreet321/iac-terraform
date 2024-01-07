#'class' is similar to an blank application form

class Railway:                          #you can name 'class' with anything, it's like opening new company
    ApplicationForm = "Candidate"           #this is like format, any variable that will be called with Candidate(), will be feeded in applicationForm

Jones = Railway()
Johanas = Railway()

print("Jones is a " + Jones.ApplicationForm)
print("Johanas is a " + Johanas.ApplicationForm)


#Now - why to use 'class' methodlogy - bcoz is becomes easy to change/understand the python code

#simple example below, imagine now the 'Railway' company takes 'ApplicationForm' for ''Employees' also


Railway.ApplicationForm = "Employee"

Michal = Railway()
Michel = Railway()

print("Michal is a " +  Michal.ApplicationForm)
print("Michel is a " + Michel.ApplicationForm)


