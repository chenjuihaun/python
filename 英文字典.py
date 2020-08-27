book={}
while True:
    print("1.建立單字")
    print("2.列出全部單字")
    print("3.翻譯")
    print("4.離開系統")
    se1=int(input("請選責工能:"))
    if se1==1:
        word=input("英文 : ")
        tran=input("翻譯 : ")
        book[word]=tran
    if se1==2:
        for eng in book.keys():
            print(eng)
    if se1==3:
        ask=input("要翻譯的英文:")
        print(book[ask])
    if se1==4:
        break   
    
    
    
    
    
    
    
    
    
    
    
    