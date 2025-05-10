f = int(input("請輸入一個整數:"))
a = "是質數"
for i in range(2, f):
    if f % i == 0:  # 輸入的數字除以會圈變數,接著拿餘數來判斷是不是0
        # 如果是0,則不是質數
        a = "不是質數"

print(f"{f} {a}")


# for    else
# 當 for 迴圈正常結束時，執行 else 區塊的程式
# example
for i in range(5):
    print(i)
else:
    print("for 迴圈正常結束")

# while   else
# 當 while 迴圈正常結束時，執行 else 區塊的程式
# example
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("while 迴圈正常結束")

# 迴圈的break 可以用來跳出所屬的迴圈,所以判斷break屬於哪個迴圈時,必須要注意縮排


import time

time.sleep(1)
s = int(input("請輸入倒數計時的秒數:"))
for i in range(s, -1, -1):
    print(i)
    time.sleep(1)
else:
    print("時間到")
