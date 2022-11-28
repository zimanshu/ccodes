## Water jug problem for 2 jugs and target capacity

q = [0]
jug1Capacity=int(input("Enter capacity of jug 1 : "))
jug2Capacity=int(input("Enter capacity of jug 2 : "))
targetCapacity=int(input("Enter the target capacity : "))
total = jug1Capacity + jug2Capacity

s = [0]
cnt = 0
flag=0
while len(q) > 0:
    size = len(q)
    cnt = cnt + 1
    for _ in range(size):
        node = q.pop(0)
        if node == targetCapacity:
            flag=1
            break
        if node + jug1Capacity <= total and node + jug1Capacity not in s:
            s.append(node + jug1Capacity)
            q.append(node + jug1Capacity)

        if node + jug2Capacity <= total and node + jug2Capacity not in s:
            s.append(node + jug2Capacity)
            q.append(node + jug2Capacity)

        if node - jug1Capacity >= 0 and node - jug1Capacity not in s:
            s.append(node - jug1Capacity)
            q.append(node - jug1Capacity)

        if node - jug2Capacity >= 0 and node - jug2Capacity not in s:
            s.append(node - jug2Capacity)
            q.append(node - jug2Capacity)
    if flag==1:
        break
if flag==0:
    print("No solution")
else:
    print("Answer : ")
    print(cnt)


## Water jug problem for N jugs and target capacity

# for 3 jugs = 3 , 5 , 7 and targetcapacity = 11
# answer = 5 steps
# 1) fill 7 lit jug (7 ltr water)
# 2) empty 3 ltr from 7 ltr jug to 3 ltr jug (7 ltr water = 4 ltr + 3 ltr)
# 3) empty 4 ltr from 7 ltr jug in 5 ltr jug (7 ltr water = 4 ltr + 3 ltr)
# 4) fill 7 ltr jug (14 ltr water = 7 ltr + 4 ltr + 3 ltr)
# 5) empty 3 ltr jug (11 ltr water = 7 ltr + 4 ltr)

jug=[]
n=int(input("Enter the number of jugs : "))
for i in range(n):
    jug.insert(i,int(input("Enter jug capacity : ")))
total=0
targetCapacity=int(input("Enter the target capacity : "))
for i in range(n):
    total=total+jug[i]
s=[0]
q=[0]
cnt=0
flag=0
while len(q)>0:
    size=len(q)
    cnt=cnt+1
    for _ in range(size):
        node=q.pop(0)
        if node==targetCapacity:
            flag=1
            break
        for i in range(n):
            if node+jug[i]<=total and node+jug[i] not in s:
                s.insert(len(s),node+jug[i])
                q.insert(len(q),node+jug[i])

            if node-jug[i]>=0 and node-jug[i] not in s:
                s.insert(len(s),node-jug[i])
                q.insert(len(q),node-jug[i])
    if flag==1:
        break
if flag==0:
    print("No solution")
else:
    print("Answer : ")
    print(cnt)