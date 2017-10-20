file=open("running-config.cfg")
list2=[]
listOFvalues=[]
dictn1=dict()
i=0
for line in file:
#if we look at file line by line  and check if "access-list" exit in the line
 if "access-list" in line:
#put whole line in variable "value" which we will use as value of dictionary 
  value=line
#split access list entry into words and put them in line
  list1=value.split()
# I know first word of accesslist enrtry is acess-list (due to syntax of access list) and second word is the name of access list so to print 
#   second entry I assigned second element of list to the key 
  key=list1[1]
  value=list1[-1]
  if key not in dictn1:
   dictn1[key]=[value]
  else:
   dictn1[key].append(value)
print(dictn1) 
