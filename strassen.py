import numpy as np


def strassen(a,b):
    k = np.size(a)
    if k==1:
        return np.dot(a,b)
    else:
        a11 = np.vsplit(np.hsplit(a,2)[0],2)[0]
        a12 = np.vsplit(np.hsplit(a,2)[1],2)[0]
        a21 = np.vsplit(np.hsplit(a,2)[0],2)[1]
        a22 = np.vsplit(np.hsplit(a,2)[1],2)[1]
        b11 = np.vsplit(np.hsplit(b,2)[0],2)[0]
        b12 = np.vsplit(np.hsplit(b,2)[1],2)[0]
        b21 = np.vsplit(np.hsplit(b,2)[0],2)[1]
        b22 = np.vsplit(np.hsplit(b,2)[1],2)[1]
        p1 = strassen(a11+a22,b11+b22)
        p2 = strassen(a21+a22,b11)
        p3 = strassen(a11,b12-b22)
        p4 = strassen(a22,b21-b11)
        p5 = strassen(a11+a12,b22)
        p6 = strassen(a21-a11,b11+b12)
        p7 = strassen(a12-a22,b21+b22)
        c11 = p1+p4-p5+p7
        c12 = p3+p5
        c21 = p2+p4
        c22 = p1-p2+p3+p6
        return np.vstack((np.hstack((c11,c12)),np.hstack((c21,c22))))

    
n=int(input())
s = 0
t = n
while t > 1:
    if t%2==1:
        t = t + 1
    t=t//2
    s=s+1
m=2**s
a=np.zeros((m,m),dtype=np.int)
b=np.zeros((m,m),dtype=np.int)
for i in range(n):
    for j,x in enumerate(map(int,input().split(' '))):
        a[i,j]=x
for i in range(n):
    for j,x in enumerate(map(int,input().split(' '))):
        b[i,j]=x
d=strassen(a,b)[:n,:n]
for i in range(n):
    st=''
    for j,x in enumerate(d[i,:]):
        st=st+str(x)+' '
    print(st)
            
        
