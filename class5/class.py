"""
使用turtle模組+for迴圈
蓋出螺旋狀的印章
"""

import turtle as t

t.pencolor("red")  # 設定顏色為紅色
t.pensize(2)  # 設定畫筆大小為2
t.fillcolor("blue")  # 設定顏色為藍色
t.begin_fill()  # 開始填充
t.end_fill()  # 結束填充
for i in range(5):
    t.forward(500)  # 向前移動
    t.right(144)  # 向右移動

t.end_fill()  # 結束填充
t.done()


# turtle.home() 是讓turtle回到原點
