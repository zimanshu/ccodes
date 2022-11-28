import copy

board=[[1,2,3],[5,6,0],[7,8,4]]
q=[[[1,2,3],[5,6,0],[7,8,4]]]
s=[[[1,2,3],[5,6,0],[7,8,4]]]
count=0
res=[[1,2,3],[5,8,6],[0,7,4]]
flag=0
while len(q)>0:
    size=len(q)
    for _ in range(size):
        v=q.pop(0)
        if v==res:
            flag=1
            break
        x=0
        y=0
        for i in range(3):
            for j in range(3):
                if v[i][j]==0:
                    x=i
                    y=j
                    break
        if x-1>=0 and y>=0:
            temp = copy.deepcopy(v)
            temp[x][y],temp[x-1][y]=temp[x-1][y],temp[x][y]
            if temp not in s:
                q.append(temp)
                s.append(temp)
        if x>=0 and y-1>=0:
            temp = copy.deepcopy(v)
            temp[x][y],temp[x][y-1]=temp[x][y-1],v[x][y]
            if temp not in s:
                q.append(temp)
                s.append(temp)
        if x+1<3 and y>=0:
            temp = copy.deepcopy(v)
            temp[x][y],temp[x+1][y]=temp[x+1][y],temp[x][y]
            if temp not in s:
                q.append(temp)
                s.append(temp)
        if x>=0 and y+1<3:
            temp = copy.deepcopy(v)
            temp[x][y],temp[x][y+1]=temp[x][y+1],temp[x][y]
            if temp not in s:
                q.append(temp)
                s.append(temp)
    count=count+1
    if flag==1:
        break
if flag==0:
    print("No Solution")
else:
    print("Answer : ")
    print(count-1)