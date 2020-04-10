i = int(input("no of inputs: "))
Input =[]
count=0
for j in range(i):
     Input.append((input()))
print(Input)
for i in range(len(Input)-2):
   
    if(len(Input)>0 and Input[i+2]=='null'):
        count+=1
        
        
if(count>0):
    print(False)
else:
    print(True)
