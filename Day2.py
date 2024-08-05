# Data structures
#list
ipl=['MI','CSK','RCB','RR']
print(ipl)
print(type(ipl))

# Indexing is supported in list

print(ipl[0])

#slicing
print(ipl[0:3])

print(ipl[1:])

ipl[1]='KKR'
ipl.append('KKR')
ipl.insert(2,'LSG')
ipl.extend([1,2])
ipl[1][0:2]
ipl[1][0:2].lower()

ipl_string="CSK,MI,RR,RCB"
ipl_list=ipl_string.split(",")
python_list=list('Python')
ipl.pop()
ipl.pop(2) # remove the 2nd value from list (count as 0,1,2)

num=[1,2,3,4,5]
print(sum(num))
print(max(num))
print(min(num))

num_str=['1','2','MI','CSK']
print(num_str)
num_str.sort()
num_str.index('CSK')