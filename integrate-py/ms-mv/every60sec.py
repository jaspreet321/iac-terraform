import time
starttime = time.time()
while True:
    print("tick")
    # Remove the Time taken by code to execute
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))
