import random


def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice


cnt = int(input("輸入丟骰子次數: "))
print(roll_dice(cnt))


# eval (input()) - 這個函式可以讓使用者輸入的文字變成程式碼執行
# 例如:
ans = eval(input("請輸入數學運算式: "))
print(ans)
# 例如輸入
# 5+3
# 顯示:8
