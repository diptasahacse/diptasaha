n=str(input("Enter your Binary number:"))
i=0
li=[]
m=[]
g=[]
        
while(i < len(n)):
    li.append(int(n[i]))
    i+=1

for i in li:
    if(i == 1 or i == 0):
        m.append(i)
    else:
        g.append(i)
if (len(li) == len(m)):
    p=0
    k=len(n)-1
    ans=0
    while(k >= 0):
        ans+=(li[p]*2**k)
        p+=1
        k-=1
    print('Decimal Answer is:',ans)
else:
    print('Wrong Binary Number')
        
    







    
    
    

    
    

