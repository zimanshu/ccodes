#!/usr/bin/env python
# coding: utf-8

# In[5]:

#   3 Missionaries and 3 Cannibals with boat capacity 2

M=3
C=3
q=[[M,C,0]]
s=[[M,C,0]]
count=0
while len(q)>0:
    size=len(q)
    flag=0
    for _ in range(size):
        m=q[0][0]
        c=q[0][1]
        state=q[0][2]
        q.pop(0)
        if m==M and c==C and state==1:
            flag=1
            break
        if state==0:
            if m>=c-1 and c>=1 and [m,c-1,1] not in s:
                q.append([m,c-1,1])
                s.append([m,c-1,1])
            if m-1>=c and m>=1 and [m-1,c,1] not in s:
                q.append([m-1,c,1])
                s.append([m-1,c,1])
            if m-1>=c-1 and c>=1 and m>=1 and [m-1,c-1,1] not in s:
                q.append([m-1,c-1,1])
                s.append([m-1,c-1,1])
            if m>=c-2 and c>=2 and [m,c-2,1] not in s:
                q.append([m,c-2,1])
                s.append([m,c-2,1])
            if m-2>=c and m>=2 and [m-2,c,1] not in s:
                q.append([m-2,c,1])
                s.append([m-2,c,1])
        else:
            if m>=c+1 and c+1<=C and [m,c+1,0] not in s:
                q.append([m,c+1,0])
                s.append([m,c+1,0])
            if m+1>=c and m+1<=M and [m+1,c,0] not in s:
                q.append([m+1,c,0])
                s.append([m+1,c,0])
            if m+1>=c+1 and c+1<=C and m+1<=M and [m+1,c+1,0] not in s:
                q.append([m+1,c+1,0])
                s.append([m+1,c+1,0])
            if m>=c+2 and c+2<=C and [m,c+2,0] not in s:
                q.append([m,c+2,0])
                s.append([m,c+2,0])
            if m+2>=c and m+2<=M and [m+2,c,0] not in s:
                q.append([m+2,c,0])
                s.append([m+2,c,0])
    count=count+1
    print([m,c,state])
    if flag==1:
        break
print(count)


# In[14]:

#   N Missionaries and N Cannibals with boat capacity 2

C=int(input())
M=C
q=[[M,C,0]]
s=[[M,C,0]]
count=0
while len(q)>0:
    size=len(q)
    flag=0
    for _ in range(size):
        m=q[0][0]
        c=q[0][1]
        state=q[0][2]
        q.pop(0)
        if m==M and c==C and state==1:
            flag=1
            break
        if state==0:
            if m>=c-1 and c>=1 and [m,c-1,1] not in s:
                q.append([m,c-1,1])
                s.append([m,c-1,1])
            if m-1>=c and m>=1 and [m-1,c,1] not in s:
                q.append([m-1,c,1])
                s.append([m-1,c,1])
            if m-1>=c-1 and c>=1 and m>=1 and [m-1,c-1,1] not in s:
                q.append([m-1,c-1,1])
                s.append([m-1,c-1,1])
            if m>=c-2 and c>=2 and [m,c-2,1] not in s:
                q.append([m,c-2,1])
                s.append([m,c-2,1])
            if m-2>=c and m>=2 and [m-2,c,1] not in s:
                q.append([m-2,c,1])
                s.append([m-2,c,1])
        else:
            if m>=c+1 and c+1<=C and [m,c+1,0] not in s:
                q.append([m,c+1,0])
                s.append([m,c+1,0])
            if m+1>=c and m+1<=M and [m+1,c,0] not in s:
                q.append([m+1,c,0])
                s.append([m+1,c,0])
            if m+1>=c+1 and c+1<=C and m+1<=M and [m+1,c+1,0] not in s:
                q.append([m+1,c+1,0])
                s.append([m+1,c+1,0])
            if m>=c+2 and c+2<=C and [m,c+2,0] not in s:
                q.append([m,c+2,0])
                s.append([m,c+2,0])
            if m+2>=c and m+2<=M and [m+2,c,0] not in s:
                q.append([m+2,c,0])
                s.append([m+2,c,0])
    count=count+1
    print([m,c,state])
    if flag==1:
        break
print(count)


# In[ ]:

#   N Missionaries and N Cannibals with boat capacity X

C=int(input())
M=C
boat=int(input())
if M+C<boat:
    print("Invalid Input")
    exit()
q=[[M,C,0]]
s=[[M,C,0]]
count=0
while len(q)>0:
    size=len(q)
    flag=0
    for _ in range(size):
        m=q[0][0]
        c=q[0][1]
        state=q[0][2]
        q.pop(0)
        if m==M and c==C and state==1:
            flag=1
            break
        if state==0:
            i=0
            j=0
            while i<=boat:
                while j<=boat:
                    if i>0 or j>0:
                        if i+j<=boat and i>=j and m-i>=c-j and m>=i and c>=j and [m-i,c-j,1] not in s:
                            q.append([m-i,c-j,1])
                            s.append([m-i,c-j,1])
                    j=j+1
                j=0
                i=i+1
        else:
            i=0
            j=0
            while i<=boat:
                while j<=boat:
                    if i>0 or j>0:
                        if i+j<=boat and i>=j and m+i>=c+j and m+i<=M and c+j<=C and [m+i,c+j,0] not in s:
                            q.append([m+i,c+j,0])
                            s.append([m+i,c+j,0])
                    j=j+1
                j=0
                i=i+1
    count=count+1
    print([m,c,state])
    if flag==1:
        break
print(count)




