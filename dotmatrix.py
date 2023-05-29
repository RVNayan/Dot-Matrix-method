import matplotlib.pyplot as pt
import numpy as np


# AA='ATGCAATAAATG'
# BB='ATGACATTAATG'


aa = open('Sequence1.txt').read()
bb = open('Sequence2.txt').read()
a=list(aa)
b=list(bb)
print("Sequence 1:",aa ,"Sequence 2:",bb)

if(len(a)>len(b)):
    f=len(a)-len(b)
    for i in range(f):
        b.append(' ')

if(len(a)<len(b)):
    f=len(b)-len(a)
    for i in range(f):
        a.append(' ')
A=a

B=b

xticks=A
yticks=B

o=list(range(len(A)))
p=list(range(len(B)))

 #reverse the list
fig, ax = pt.subplots()
ax.plot(o,p,'white')
ax.set_xticks(o)
ax.set_xticklabels(xticks)

ax.set_yticks(p)
ax.set_yticklabels(yticks)

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            m=a[i]+str(i)
            a[i]=m
    
            

for i in range(len(b)-1):
    for j in range(i+1,len(b)):
        if(b[i]==b[j]):
            m=b[i]+str(i)
            b[i]=m
X=[]
Y=[]

for x in range(len(A)):
    for y in range(len(B)):
        x1=a[x]
        y1=b[y]
        
        if(x1[0]==y1[0]):
            X.append(x1)
            Y.append(y1)
            
        else:
            X.append('')
            Y.append('')

def check(x1,y1,xpos,ypos,lex,ley):
    xc=xpos
    yc=ypos
    x11=x1[xc][0]
    y11=y1[yc][0]
    while(x11==y11):  
            x11=x1[xc][0]
            y11=y1[yc][0]
            if(xc<lex-1 and yc<ley-1 and x11==y11):  
               
                xc=xc+1
                yc=yc+1

            elif(xc==lex-1 and x11==y11):
                xc=xc
                yc=yc
            
                break
            elif(yc==ley-1 and x11==y11):
                yc=yc
                xc=xc
                break

            else:
                xc=xc-1
                yc=yc-1

                break
            
    return xc,yc





# print(X,Y)
pt.plot(A,B,'white')
pt.scatter(X,Y) #points
d={}
for x in range(len(A)):
    for y in range(len(B)):
        m,n=check(a,b,x,y,len(a),len(b))
        if(m-x>0 and n-y>0):
            pt.plot([x,m],[y,n],'k')
            
            d[x,y]=[m,n]
        
pt.xlim(-1,len(A)-0.5)
pt.ylim(-1,len(B)-0.5)

xnew=[]
xo=0
############################### 
for i in range(len(X)):
    if(i%len(A)==0):
        xnew.append(X[i:i+len(B)])
x2new=[]

for i in range(len(A)):
    xx=[]
    for j in range(len(xnew)):
        xx.append(xnew[j][i])
    x2new.append(xx)
xnew=x2new

pt.title("Dot-Matrix")
pt.grid()
pt.show()
