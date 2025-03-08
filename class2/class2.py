# 字串運算
a = "Hello"
b = "World"
c = a + " " + b  # 字串相加
print(c)

a = a * 3  # 字串乘法
print(a)

# 認識基本指令
# 指令會有名稱跟括號組成，()裡面放提供給指令的參數
# 每個參數都要用逗號隔開
m = max(1, 2, 3, 4, 5)  # 取最大值
print(m)

le = len("hello")  # 取長度
print(le)

# type()取得參數的型態
print(type(1))  # 取型態
print(type("hello"))  # 取型態
print(type(1.0))  # 取型態
print(type(True))  # 取型態

# 型態轉換
# int()轉換成整數
# float()轉換成浮點數
# str()轉換成字串
# bool()轉換成布林

print(int("123"))  # 123
print(int(123.9999))  # 123
print(int(True))  # 1
print(int(False))  # 0
print("-------------")

print(float("123.456"))  # 123.456
print(float(123))  # 123.0
print(float(True))  # 1.0
print(float(False))  # 0.0
print("-------------")

print(str(123))  # 123
print(str(123.456))  # 123.456
print(str(True))  # True
print(str(False))  # False
print("-------------")

print(bool(123))  # True
print(bool("123"))  # True
