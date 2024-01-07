#"OPEN" module in python act as file I/O, means ready a file in an folder through python

#Below command just takes input for file 'f', where first enrty is filename, followed by 'r' means 'read'

f = open('sample_file-OPEN.txt', 'r')
data = f.read()                                       #below command takes variable 'data' & perform's some action on above 'f' file
print(data)                                           #simple print the value 'data' variable
f.close()                                             #this command closes the file mentioned under 'f' above - IF YOU DONT CLOSE THIS FILE, OTHER PERSON MAY NOT BE ABLE TO READ/WRITE IN THAT FILE

