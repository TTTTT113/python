# 複製 List ，避免原本的 List 被修改
L = ["hello", "world"]
L2 = L.copy()  # 使用 copy()複製 List
print(L2)  # ['Hello', 'World']
L2[0] = "python"  # 修改複製後 List 的索引0資料
print(L)  # ['Python', 'World'] 原本的 List 不會被修改
print(L2)  # [Python', 'World'] 只有複製的 List 會被修改
# 這跟變數的=賦值不同, 一般情況下會開2個記憶體空間,
# 在List的情況下使用=會讓兩個變數名稱指向同一個記憶體空間
# 這導致修改一個 List 會影響到另一個 List
# 所以在需要複製 List 時 , 應該使用 copy() 方法

# pop :移除並回傳 List 中的元素
L = ["hello", "world", "python"]
# 不給索引時 , pop() 會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # ['Hello', 'World']
s = L.pop(0)  # 移除索引 1 的元素,並回傳該值
print(s)  # 'Hello'
print(L)  # ['World']


L = []
while True:
    print(L)
    print("1.新增東西")
    print("2.修改東西")
    print("3.刪除東西")
    print("4.離開程式")
    T = input("請輸入你的選擇 (1-4)：")
    if T == "1":
        print("a. 加到尾端")
        print("b. 插入指定位置")
        M = input("請選擇方法 (a/b)：")
        O = input("請輸入要新增的物品：")
        if M == "a":
            L.append(O)
        elif M == "b":
            P = input("請輸入位置 (0 為第一個)：")
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
        f = input("請選擇方法 (a/b)：")
        if f == "a":
            L.remove(e)
        elif f == "b":
            g = input("請輸入要刪除的物品編號：")
            L.pop(int(g))
    elif T == "4":
        break
