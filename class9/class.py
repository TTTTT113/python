import random as a  # 這是隨機模組

# random.randrange 設定範圍的方式跟 range一樣，特性也不一樣包含最後一個數字
# random.randrange 的功能是隨機取得一個數字，range是產生一組數字
print(a.randrange(10))  # 從0到9的隨機數
print(a.randrange(1, 10))  # 從1到9中隨機取得一個數字
print(a.randrange(1, 10, 2))  # 從[1,3,5,7,9]中隨機取得一個數字

# random.randint 設定範圍的方式必須要用有開始跟結束, 且包含最後一個數字
# 不能跳數字抽籤
print(a.randint(1, 10))  # 從1到10的隨機數


import random

f = random.randint(1, 100)  # 從1到100的隨機數
while True:
    i = int(input("請輸入一個1到100的整數: "))
    if i == f:
        print("恭喜你，正確答案")
        break
    elif i > f:
        print("在小一點")
    elif i < f:
        print("在大一點")


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


# list清單 (list)
# list 可以存入很多資料,每筆用','分隔
# list 可以存入不同型態的資料
# list 最外層用'[]'包起來
L = [
    1,
    2,
    3,
    4,
    5,
]  # 數字
print(L)
L = [1, 2, 3, 4, 5, "hello"]  # 數字字串LIst
print(L)


# List取值
# List 取值方式跟字串一樣,用'[]'取值
# List 取值方式跟字串一樣,也可以用'[:]'取值
# List 當中資料的編號(index)以0為開頭
L = [
    1,
    2,
    3,
    4,
    5,
]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值


# List 取值方式跟字串一樣 , 也可以用'[:]'取值
# 設定範圍的方式跟range很像,不包含最後一個數字
print(L[1:4:2])  # 取得第2個到第4個值,且間隔為2
print(L[0:3])  # 取得第1個到第3個值
print(L[:3])  # 取得第1個到第3個值
print(L[3:])  # 取得第4個到最後一個值
print(L[:])  # 取得所有值


# List 取值方式跟字串一樣 , 也可以用'[:]'取值

# List len 列表長度
L = [
    1,
    2,
    3,
    4,
    5,
]
print(len(L))  # 取得List的長度,也就是List當中幾筆資料

# 務必不要跟index混淆, index是資料的編號, len是資料的數量

# len 可以搭配 for 迴圈使用來取得List的所有資料
for i in range(len(L)):  # 這邊的i是index
    print(L[i])

# 要使用哪一種方式讀取List當中的資料, 要看使用的情境當會不會需要index


j = juice = [".蘋果汁, 柳橙汁, 葡萄汁,系統關閉"]


while True:
    for i in range(len(juice)):
        print(f"{i + 1}.{juice[i]}")
    try:
        n = int(input("請輸入編號"))
    except:
        print("輸入錯誤查無此商品,請重新輸入")
        continue
    if n == len(juice):
        print("系統關閉")
        break
    elif 1 <= n < len(juice):
        print(f"您點的商品是{juice[n - 1]}")
    else:
        print("輸入錯誤查無此商品,請重新輸入")
