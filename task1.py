import string
list1=[]
book1=open("Book1.txt")
dict1={}
book1length=0
book2length=0
book3length=0
result1=[]
result2=[]
result3=[]
for line1 in book1:
 line1.strip()
 line1.strip(string.punctuation)
 words1=line1.split(" ")
 for i in words1:
  if i not in dict1:
   dict1[i]=1
  else:
   dict1[i]+=1
for i in dict1:
 list1.append(i)
for i in list1:
 length=len(i)
 if length>book1length:
  book1length=length
  longestWord=i 
result1.append(longestWord)
result1.append(book1length)
print("longest word in book1 is ",result1)





book2=open("Book2.txt")
dict2={}
for line2 in book2:
 line2.strip()
 line2.strip(string.punctuation)
 words2=line2.split(" ")
 for i in words2:
  if i not in dict2:
   dict2[i]=1
  else:
   dict2[i]+=1
for i in dict2:
 list1.append(i)
for i in list1:
 length=len(i)
 if length>book2length:
  book2length=length
  longestWord=i 
result2.append(longestWord)
result2.append(book2length)
print("longest word in book2 is ",result2)



book3=open("Book3.txt")
dict3={}
for line1 in book3:
 line1.strip()
 line1.strip(string.punctuation)
 words1=line1.split(" ")
 for i in words1:
  if i not in dict3:
   dict3[i]=1
  else:
   dict3[i]+=1
for i in dict3:
 list1.append(i)
for i in list1:
 length=len(i)
 if length>book3length:
  book3length=length
  longestWord=i 
result3.append(longestWord)
result3.append(book3length)
print("longest word in book3 is ",result3)
