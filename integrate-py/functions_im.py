#functions starts with 'def' & function can be called anytime in the script to perform it role, same as gitlab pipeline
# variable 'i' has been assigned with a formula & this formula will be called many times in the script

def add(number):
    i = (number[0] + number[1])
    return i


number1 = [23, 46]
addition1 = add(number1)    #this is where it is calling the funtion & applied the function on 'number1'

number2 = [23, 45]
addition2 = add(number2)    #this is where it is calling the funtion & applied the function on 'number2'

number3 = [23, 44]
addition3 = add(number3)    #this is where it is calling the funtion & applied the function on 'number3'

print(addition1)
print(addition2)
print(addition3)


##In simple terms, function in python stores the 'formula' that whole script will reuse as many times

def greet(name):
    p = ("have a good day" + " " +  name)
    return p

name = "boston"
greet1 = greet(name)

print(greet1)


def greet(name):
    p = ("have a good day" + " " + name)
    return p

abc = "paddy"
greet2 = greet(abc)

print(greet2)


