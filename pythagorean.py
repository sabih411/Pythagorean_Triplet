total=1000
list_=[]
for a in range(1,int(total/3)+1,1):
  for b in range(a+1,int(total/2)+1,1):
    c=total-a-b;
    if(a*a+b*b==c*c):
      list_.append(a)
      list_.append(b)
      list_.append(c)
print(list_[0]*list_[1]*list_[2])
