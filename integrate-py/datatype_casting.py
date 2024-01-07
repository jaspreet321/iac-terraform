#here 35464 is considered as 'string', not as 'integer/number'
#Because 35464 is under 'double-quotes" & string is always in quotes
xyz = "35464"
abc = 46229
jkh = 6573

#check the datatype of mentioned variable 'xyz' & 'abc'
print(xyz)
print(type(xyz))
print(abc)
print(type(abc))
print(jkh)
print(type(jkh))

#change variable 'xyz' from string to integer
xyz = int(xyz)
abc = str(abc)
jkh = float(jkh)

#now check again datatyoe of mentioned variable 'xyz'
print(type(xyz))
print(xyz)
print(type(abc))
print(abc)
print(type(jkh))
print(jkh)

