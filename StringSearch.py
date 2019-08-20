def search(list,a):
    print(list)
    if a in list:
        return True
    else:
        return False
list=[]
while True:
        a=int(input("Enter the element"))
        if a!=-1:
            list.append(a)
        else:
            break
b=input("Ënter the element to be searched")
print(search(list,int(b)))
