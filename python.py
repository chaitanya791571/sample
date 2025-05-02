def addmatrix(m1,m2):
  rows = len(m1)
  columns=len(m[0])
  res=[[0 for i in range(columns)] for j in range(rows)]
  for i in range(rows):
     for j in range(columns):
        res[i][j]=m1[i][j]+m2[i][j]
 
      return res
m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
m2=[[10,11,12],
    [13,14,15],
    [16,17,18]]
r=addmatrix(m1,m2)
for row in r :
  for element in row:
    print(element,end='\t')
  print()