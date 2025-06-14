# index: 尋找指定元素在List,中第一次出現的位置
# 如果元素不存在會產生錯誤,所以使用前建議先檢查元素是否存在
L = [1, 3, 2, 4, 5]
print(L.index(3))  # 找出數字 3 在索引位置 1

# count:統計某個元素在List中總共出現了幾次
# 這個方法很適合用來檢查重複資料的數量
L = ["hello", "world", "Python", "hello"]
print(L.count("hello"))  # "hello"這個字串總共出現2次

# sort:將List 中的元素進行排序,預設是由小到大(升序排列)
# 注意:這個方法會直接修改原本的List,如果不想這樣做,不會產生的 List
L = [1, 3, 2, 4, 5]
L.sort()
print(L)

# sort(reverse=True):將List 中的元素進行排序,預設是由大到小(降序排列)
# .sort(reverse=True)參數可以讓排序結果相反
L = [1, 3, 2, 4, 5]
L.sort(reverse=True)
print(L)

# reverse:將List 中的元素的順序完全顛倒
# 這不是排序!只是把第一個變最後一個,最後一個變第一個
L = [1, 3, 2, 4, 5]
L.reverse()
print(L)

# List和字串有很多相似的操作方式
# 我們可以像操作字串一樣來處理 List

# 合併兩個 List : 使用 + 運算子將兩個List 合併
# 這會產生一個全新的List,原本的 List 不會被修改
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # 把L1 和 L2 合併成一個新的List
print(L3)

# 重複 List 中的內容 : 使用 * 運算子讓 List 內容重複多次
# 這在需要建立重複資料時很有用
L = [1, 2, 3]
L = L * 3  # 重複 List 中的內容3次
print(L)

# 不同資料型態之間的轉換不同資料型態之間的轉換技巧
print(range(10))  # range 物件本身看不到具體內容,只是一個範圍描述
print(list(range(10)))  # 可以將range物件轉換成list,並且可以看到具體內容
print(list("hello"))  # 將字串轉換成List,每個字元都會變成獨立的元素

# split: 將一個完整的字串按照指定的分隔符號切割多個部分
# 這是處理文字資料時非常常用的方法
s = "hello world"
L = s.split()  # 以空白字元作為分隔點來切割字串
print(L)
calendar = "2020/12/25"
L = calendar.split("/")  # 以斜線作為分隔點來切割日期字串
print(L)

# join: 將List中的多個字串元素合併成一個完整的字串
# 可以指定要用甚麼符號來連接這些元素
L = ["hello", "world"]
s = " ".join(L)  # 以空白字元作為連接點來合併字串
print(s)

日期 = input("請輸入你的生日:")
日期 = 日期.split("/")
日期 = "-".join(日期)
print(日期)
