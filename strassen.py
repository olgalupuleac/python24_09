import numpy as np
import math

def strassen(a,b,k):
   if k==1:
       return np.dot(a,b)
   else:
       p1=strassen(a[:k//2,:k//2]+a[k//2:,k//2:],b[:k//2,:k//2]+b[k//2:,k//2:],k//2)
       p2=strassen(a[k//2:,:k//2]+a[k//2:,k//2:],b[:k//2,:k//2],k//2)
       p3=strassen(a[:k//2,:k//2],b[:k//2,k//2:]-b[k//2:,k//2:],k//2)
       p4=strassen(a[k//2:,k//2:],b[k//2:,:k//2]-b[:k//2,:k//2],k//2)
       p5=strassen(a[:k//2,:k//2]+a[:k//2,k//2:],b[k//2:,k//2:],k//2)
       p6=strassen(a[k//2:,:k//2]-a[:k//2,:k//2],b[:k//2,:k//2]+b[:k//2,k//2:],k//2)
       p7=strassen(a[:k//2,k//2:]-a[k//2:,k//2:],b[k//2:,:k//2]+b[k//2:,k//2:],k//2)
       np.vstack((np.hstack((p1+p4-p5+p7,p3+p5)),np.hstack((p2+p4,p1-p2+p3+p6))))
       return np.vstack((np.hstack((p1+p4-p5+p7,p3+p5)),np.hstack((p2+p4,p1-p2+p3+p6))))
   
   
   

    
n=int(input())
k=2**math.trunc(math.log(float(2*n-1),2))
a=np.zeros((k, k))
b=np.zeros((k, k))
for i in range(n):
    l=list(map(float,input().split(' ')))
    for j in range(n):
        a[i][j]=l[j]
for i in range(n):
    l=list(map(float,input().split(' ')))
    for j in range(n):
        b[i][j]=l[j]
print(strassen(a,b,k)[:n,:n])
print(np.dot(a,b)[:n,:n])


