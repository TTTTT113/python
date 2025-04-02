import turtle as t

t.penup()  #提筆,這樣就不會畫線但是可以移動
t.color("red")  #設定顏色為紅色
t.shape("turtle")  #設定形狀為烏龜
for i in range(120):
    t.forward(20)
    t.stamp()#蓋一個印章
    t.right(6)  

t.done()