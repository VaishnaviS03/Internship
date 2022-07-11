li=[[1,2,3,4],[5,6,7,8]]
li2=[[9,10,11,12],[13,14,15,16]]
li3=[[],[]]
for i in range(len(li)):
    for j in range(len(li[0])):
        x=li[i][j]+li2[i][j]
        li3[i].insert(j,x)
print("List containing sum of corresponding elements of the given two lists:",li3)
        
