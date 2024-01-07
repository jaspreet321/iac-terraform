import  threading

def printit():
    second = 1
    while threading.Timer(1, printit).start(): #for every second that pass.
        print(second)
        second += 1

printit()
