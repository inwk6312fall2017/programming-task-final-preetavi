# + is used to create a file if it doesn't exist, a is used to append to the file
newfile=open("RUNNING-CONFIG.cfg","a+")
#open file you want to read from
file=open("running-config.cfg")
for line in file:
#it takes each line in the file finds "172." and replaces it with "192." .   put edited lines in "editedLine" 
 editedfile=line.replace("172.","192.")
#newfile object is used to access the newly created file and we pass edited code to write it in new file 
 newfile.write(editedfile)

#used cat to read "RUNNING-CONFIG.cfg 
