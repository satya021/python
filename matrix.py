   X = [[6,2,3],
    [6 ,5,6],
    [7 ,3,9]]
 
Y = [[1,8,7],
   
   
    [6,8,4],
    [3,9,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
for i in range(len(X)):  
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)