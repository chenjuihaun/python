num=int(input('班上有多少人?'))
math=[]
name=[]
for i in range(num):
    student=input('姓名?')
    score=int(input('成績?'))
    math.append(score)
    name.append(student) 
highest=0
lowest=100
avg=0
highman=''
lowman=''
#i : 0~num-1
for i in range(num):
    if highest <math[i]:
        highest=math[i]
        highman=name[i]
    if lowest >math[i]:
        lowest=math[i]
        lowman=name[i]
    avg=avg+math[i]
print('平均=',avg/num)        
print('最高=',highest,highman)
print('最低=',lowest,lowman)                  