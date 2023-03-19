X = [[90,80,70],
     [60,50,40],
     [30,20,10]]

Y = [[10,20,30],
     [30,40,50],
     [60,70,80]]

T = [[0,0,0],
    [0,0,0],
    [0,0,0]]
        
F = [[0,0,0],
    [0,0,0],
    [0,0,0]]
        
C = [[0,0,0],
    [0,0,0],
    [0,0,0]]

B = [[0,0,0],
    [0,0,0],
    [0,0,0]]


for i in range(len(X)):
    for j in range(len(X[0])):
        T[i][j] = X[i][j] + Y[i][j]
        F[i][j] = X[i][j] - Y[i][j]
        C[i][j] = X[i][j] * Y[i][j]
        B[i][j] = X[i][j] // Y[i][j]
    
print("\nTOPLAMA")
for t in T:
    print(t)
print("\nFARK")
for f in F:
    print(f)
print("\nÇARPMA")
for c in C:
    print(c)
print("\nBÖLME")
for b in B:
    print(b)