import random
ans=random.randint(1,20)
i=0
while i<5:
    num=int(input("input a num"))
    if num>ans:
        print("太大了")
    elif num<ans:
        print("太小了")
    else:
        print("玩了",i+1,"次")
        break  
    i=i+1
    
    
    
    