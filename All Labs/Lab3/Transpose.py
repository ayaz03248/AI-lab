first =[[0,0,0,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,0,1,1,0]]
second =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(0,5):
    for j in range(0,5):
       p = first[i][j]
       if( p ==1):
            second[j][i] = p;
print(second);