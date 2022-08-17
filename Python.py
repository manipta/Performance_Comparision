f=open('my_file.txt','r')
for i in f:
	ch=i
	count=count+1
print(count)
f.close()