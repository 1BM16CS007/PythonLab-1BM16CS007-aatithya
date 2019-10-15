for i in range(100,401):
i1 = i%10
temp=int(i/10)
i2=temp%10
i3=int(temp/10)
if i1%2==0 and i2%2==0 and i3%2==0:
print(i+",",end="")