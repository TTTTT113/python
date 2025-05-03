jump = int(input("請輸入跳繩的次數"))
# 跳繩
for i in range(1, jump + 1):
    if i % 10 == 0:
        print("休息一下")
        continue
    print(f"第{i}次的跳繩")