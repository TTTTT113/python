# 1新增一個變數total, 用來計算總金額
# 新增一個使用者目前輸入的商品價格
# 使用while迴圈,當使用者輸入的商品價格不等於零時，
# 就會執行回圈內的程式


f = int(input("請輸入價格:"))
sum = 0
while f != 0:
    sum = sum + f
    f = int(input("請輸入價格:"))
