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