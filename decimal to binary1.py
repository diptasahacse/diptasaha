def dec_bin(n,l):
    while(n != 0):
        if(n%2 == 0):
            l.append(0)
        else:
            l.append(1)
        n=n//2
    k=li[::-1]
    print('Binary Number is')
    for i in k:
        print(i)
li=[]
p=int(input('Enter decimal number:'))
dec_bin(p,li)
