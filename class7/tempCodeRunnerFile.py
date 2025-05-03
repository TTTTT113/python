import time

time.sleep(1)
s = int(input("請輸入倒數計時的秒數:"))
for i in range(s, -1, -1):
    print(i)
    time.sleep(1)
else:
    print("時間到")
