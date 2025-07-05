# def
# 新增一個函數要用 def 開頭 , 後面接著函數名稱 , 再加上小括號 , 最後加上冒號
# 小括號裡面可以放入傳入函數的參數也可以不放
def hello():
    print("hello", "world")


for i in range(10):
    hello()


# 有傳入參數的函數
# 這個函數已由個參數 name 當呼叫這個函數時 , 可以傳入一筆資料給 name
def hello(name):
    print(f"hello, {name}!")


hello("alice")
hello("bob")
hello("charlie")
for i in range(10):
    hello(i)  # 這裡的I會被當作 name 的值


# 有回傳值得函數
# 這個函數會回傳一個值 , 當呼叫這個函數時 , 可以把回傳的值存起來
# 在指令當中只要執行return 就會回傳值 , 並結束函數
def add(a, b):  # 可以允許多個傳入參數
    return a + b


print(add(1, 2))
print(add("hello", "world"))
sum = add(3, 4)  # 可以將回傳值存到變數中
print(sum)


# 有多個回傳值的函數
# 這個函數會回傳兩個值 , 當呼叫這個函數時 , 可以把回傳的值存起來
def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)  # 可以將回傳值存到多個變數中
print(f"sum = {sum}, sub = {sub}")


# 多個 return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))


# 預設參數
# 可以在函數的參數中的設定預設值 , 當呼叫這個函數時 , 如果沒有傳入值 , 就會使用預設值
# 多個參數時 , 有預設值的參數要放在沒有預設值的參數後面
def hello(name, message="hello"):
    print(f"{message}, {name}!")


# 如果是 def hello(message = "hello", name) ,會出錯 , 因為有預設值的參數要放在沒有預設值的參數後面
hello("alice")
hello("bob", "good morning")


# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數 area 是區域變數
    # length = length + 1 #這行會出錯 ,
    # 因為在函數內部length 是區域變數 , 不能直接修改全域變數
    print("面積是", area)


calculate_square_area()
# print("長度是", area) #這行會出錯 , 因為area 是區域變數 , 只能在函數內部使用

length = 5  # 區域變數


def calculate_square_area():
    area = length**2  # length 是全域變數 area 是區域變數
    print("面積是", area)


length = 10  # 全域變數
calculate_square_area()  # 面積是100
# 因為要等到函數被呼叫時才會執行 , 所以area的值是在函數被呼叫時才會被計算


length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2  # length 是全域變數 area 是區域變數


calculate_square_area()
print("面積是", area)  # 面積是100
# 這時候指令內部的area 是區域變數  , 不會影響到全域變數的值

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area() -> int:
    area = length**2  # length 是全域變數 area 是區域變數
    return area


area = calculate_square_area()
print("面積是", area)  # 面積是25

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    global area  # 使用 global , 將area變成全域變數, 可以在函數內部修改全域變數的值
    area = length**2  # length 是全域變數 area 是區域變數


calculate_square_area()
print("面積是", area)  # 面積是25


def hello(name: str):  # 函數傳入參數都是區域變數
    """
    指令說明區\n
    這是一個打招呼的函數\n
    參數:\n
    name: str - 姓名

    回傳 : none

    範例:hello("alice") # hello alice
    """
    print(f"hello, {name}!")
