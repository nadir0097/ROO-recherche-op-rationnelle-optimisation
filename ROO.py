import numpy
w=int
n=int
c=13
t=int
i=9
s=0
for i in range(0, w):
    t[0, c] = 0
for i in range(0, n):
    for i in range(0, w):
        if (c >= w[i]):
            t[i, c] = max(t[i-1, c], t[i-1, c-w[i]] + x[i])
        else:
            t[i, c] = t[i-1, c]
while t[i,j]==t[i,j-1]:
      
     while j>0:
           while i>0 and t[i,j]==t[i-1,j]:
           
                 j=j-poisobjet[i]
           if s >= 0 :
              ajoute-objet(objet[i])
       
print(s)
