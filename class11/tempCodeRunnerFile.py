L = []
while True:
    print(L)
    print("1.新增東西")
    print("2.修改東西")
    print("3.刪除東西")
    print("4.離開程式")
    T = (input("請輸入你的選擇 (1-4)："))
    if T == "1":
        print("a. 加到尾端")
        print("b. 插入指定位置")
        M = (input("請選擇方法 (a/b)："))
        O = (input("請輸入要新增的物品："))
        if M == "a":
            L.append(O)
        elif M == "b":
            P = (input("請輸入位置 (0 為第一個)："))
            L.insert(int(P), O)
        elif T == "2":
             c = input("請輸入要修改的物品編號：")
             d = input("請輸入新的物品：")
             L[int(c)] = d
        elif T == "3":
            e = input("請輸入要刪除的物品名稱：")
            L.remove(e)
            print("a.依名稱刪除")
            print("b.依位置刪除")
            f = (input("請選擇方法 (a/b)："))
            if f == "a":
                L.remove(e)
            elif f == "b":
                g = input("請輸入要刪除的物品編號：")
                L.pop(int(g))
        elif T == "4":
            break