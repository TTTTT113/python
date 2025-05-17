import random

big = 100
small = 1
f = random.randint(1, 100)  # 從1到100的隨機數
while True:
    i = int(input(f"請輸入一個{small}到{big}的整數: "))
    if i == f:
        print("恭喜你，正確答案")
        break
    elif i > f:
        print("在小一點")
        if i < big:
            big = i
    elif i < f:
        print("在大一點")
        if i > small:
            small = i