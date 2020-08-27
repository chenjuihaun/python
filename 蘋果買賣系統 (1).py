apple=0
price=0
while True:
    print('1. 設定')
    print('2. 進貨')
    print('3. 出貨')
    print('4. 營業額統計')
    print('5. 庫存統計')
    sel=int(input('請選擇功能 :'))
    if sel==1:
        apple=int(input('蘋果數量 : '))
        price=int(input('蘋果價格 : '))
    if sel==2:
        apple==apple+int(input('進貨數量'))
    if sel==3:
        sell=int(input('出貨數量'))
        apple=apple-sell
    if sel==4:
        print('賣出:',sell,'顆,共',sell*price,'元')
    if sel==5:
        print('剩下數量',apple)        