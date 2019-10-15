str1=input("Enter the binary sequence: ")
lis = str1.split(",")
str2=""
for i in range(len(lis)):
if int(lis[i],2)%5==0:
str2+=lis[i]+","

print ("Output is: ",str2[:len(str2)-1])