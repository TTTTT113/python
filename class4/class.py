n = int(input("請輸入一個整數: "))

if n % 2 == 0:
    print((f"{n}是偶數"))
else:
    print((f"{n}是奇數"))
# f=format可以在字串裡放入任何型態的資料,每一筆資料都要用{}來包起來
# 如果想要在字串裡插入數字,可以用{}格式化
# 匯入模組
import turtle  # 匯入模組turtle

turtle.forward(100)  # 向前移動100個單位
turtle.done()  # 讓視窗不要關閉

import turtle as t  # 匯入模組turtle並取別名為t

t.speed(1)  # 設定速度為1
t.forward(100)  # 向前移動100個單位
t.right(90)  # 向右轉90度
t.forward(100)  # 向前移動100個單位
# 發現turtle一開始面向右邊
t.done()  # 讓視窗不要關閉


# 匯入模組
import turtle  # 匯入模組turtle

turtle.forward(100)  # 向前移動100個單位
turtle.done()  # 讓視窗不要關閉

import turtle as t  # 匯入模組turtle並取別名為t

t.speed(1)  # 設定速度為1
t.forward(100)  # 向前移動100個單位
t.right(90)  # 向右轉90度
t.forward(100)  # 向前移動100個單位
t.right(90)
t.forward(100)  # 向前移動100個單位
t.right(90)  # 向右轉90度
t.forward(100)
# 發現turtle一開始面向右邊
t.done()  # 讓視窗不要關閉
# for迴圈是次數型的循環
# range會產生出一組數字，range不會數到最後的數字


# for的組成有三個部分
# for 迴圈變數 in 範圍:
# 迴圈變數只能活在for迴圈裡面
# 迴圈變數每回合都會從範圍中取出一個值
for i in range(6):  # range 可以產生一組數字, 0~5
    print(i)

for i in range(1, 6):  # range = 1~5
    print(i)

for i in range(1, 6, 2):  # range = 1, 3, 5
    print(i)


import turtle as t  # 匯入模組turtle並取別名為t

t.speed(1)  # 設定速度為1
for i in range(4):  # range 可以產生一組數字, 0~5
    t.forward(100)  # 向前移動100個單位
    t.right(90)
t.done()  # 讓視窗不要關閉


# 參考code
import turtle as t

t.penup()  # 提筆,這樣就不會畫線但是可以移動
t.color("red")  # 設定顏色為紅色
t.shape("turtle")  # 設定形狀為烏龜
for i in range(120):
    t.forward(20)
    t.stamp()  # 蓋一個印章
    t.right(6)

t.done()


import turtle as t
import time

t.speed(0)
for j in range(60):
    t.right(6 * j)
    t.forward(80)
    time.sleep(1)
    t.home()
    t.left(90)
    t.clear()

t.done()


import time

n = int(input("請輸入正整數: "))
for i in range(1, n + 1):
    if i % 3 == 0 or i % 7 == 0:
        print(i)


"""
EX:
請輸入要印出的箭頭:3
  *
 ***
*****
"""
n = int(input("請輸入要印出的箭頭大小:"))
for i in range(1, n + 1):
    print(f" " * (n - i) + "*" * (2 * i - 1))  # 上半部分
    # 如何把i=1,2,3變成 2, 1, 0==>n-i==>這個可以拿來畫空格
    # 如何把i=1,2,3變成 1, 3, 5==>2*i-1==>這個可以拿來畫星星
for i in range(1, n + 1):
    print(f" " * (n - 1) + "*")
