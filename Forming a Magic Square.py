a=[]
count=0
b=[]
c=[]
def icheck(a,b):
         
         for i in range(3):
                  count=0
                  for j in range(3):
                           count=count+int(a[i][j])
                  b.append(count)
         return(b)
def jcheck(a,c):
         for j in range(3):
                  count=0
                  for i in range(3):
                           count=count+int(a[i][j])
                  c.append(count)
         return(c)

for i in range(3):
         a.append(list(input().split()))
b=icheck(a,b)
c=jcheck(a,c)
print(b)
print(c)
         
"""
a=[]
count=0
b=[]
c=[]
def icheck(a,b):
         
         for i in range(3):
                  count=0
                  for j in range(3):
                           count=count+int(a[i][j])
                  b.append(count)
         return(b)
def jcheck(a,c):
         for j in range(3):
                  count=0
                  for i in range(3):
                           count=count+int(a[i][j])
                  c.append(count)
         return(c)

for i in range(3):
         a.append(list(input().split()))
b=icheck(a,b)
c=jcheck(a,c)
print(b)
print(c)
for i in range(3):
         if(int(b[i])>15 and int(c[i])>15):
                  a[i][i]=int(a[i][i])+(int(b[i])-15)
         elif(int(b[i])<15 and int(c[i])<15):
                  a[i][i]=int(a[i][i])-(int(b[i])-15)
         elif(int(b[i])==15 and int(c[i])==15):
                  a[i][i]=int(a[i][i])
for i in range(3):
         for j in range(3):
                  print(a[i][j],end=" ")
         print("")
"""
