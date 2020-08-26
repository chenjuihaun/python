import random
ans=random.randint(1,20)
i=0
while i<5:
    num=int(input("請輸入0到20之間的數字:"))
    if num>20 or num<0:
        print("喔歐輸入錯誤，輸入錯誤")
        print("請輸入0到20之間的數字喔!")
    elif num>ans:
        print("喔歐!")
        print("太大了喔!")
    elif num<ans:
        print("喔歐!")
        print("太小了喔!")
    else:
        print("恭喜你答對了!")
        print("你總共玩了",i+1,"次")
        break  
    i=i+1
