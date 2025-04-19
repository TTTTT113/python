"""
使用turtle模組+for迴圈
蓋出螺旋狀的印章
"""

import turtle as t

t.speed(0)
t.penup()  # 提筆,這樣就不會畫線但是可以移動
for i in range(13):
    t.forward(100)
    t.stamp()
    t.home()
    t.right(30 * i)
t.done()
