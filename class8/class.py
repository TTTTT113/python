# 迴圈的 break 可以用來跳出所屬的迴圈， 所以判斷break屬於哪個迴圈時，必須要注意縮排
# 例如:

for i in range(5):
    for j in range(5):
        if i == 2:
            break
        print(f"i:{i}, j:{j}")
        # 這裡的break只會跳出內的層的for迴圈，外層的 for 迴圈還是會繼續執行


while True:
    print("1.蘋果汁")
    print("2.柳橙汁")
    print("3.葡萄汁")
    print("4.系統關閉")
    n = input("請輸入編號")
    if n == "1":
        print("蘋果汁")
    elif n == "2":
        print("柳橙汁")
    elif n == "3":
        print("葡萄汁")
    elif n == "4":
        print("系統關閉")
        break
    else:
        print("查無此項目")

# continue
# 迴圈的 continue 可以用來跳過當前的迴圈，繼續執行下一次的迴圈
for i in range(5):
    if i == 2:
        continue
    print(i)
# 這裡的 continue 會跳過 i = 2 的那次迴圈，直接執行 i = 3 的那次迴圈
# 所以輸出的結果也是0，1，3，4
# continue 也可以用在while迴圈中
# 例如:
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)
    i += 1
# continue 也要判斷所屬的迴圈，所以要注意縮排


jump = int(input("請輸入跳繩的次數"))
# 跳繩
for i in range(1, jump + 1):
    if i % 10 == 0:
        print("休息一下")
        continue
    print(f"第{i}次的跳繩")
