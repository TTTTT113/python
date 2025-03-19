# try except
# 錯誤處理
try:
    # 嘗試執行可能會出錯的程式碼
    f = int(input("input a number: "))

except:
    # 如果有錯誤發生，執行這段程式碼
    print("you should input a number")

else:
    # 如果沒有錯誤發生，執行這段程式碼
    print(n + 1)

# 以作業為例
try:
    h = float(input("請輸入身高: "))
    w = float(input("請輸入體重: "))
    bmi = w / h**2
    print(f"你的BMI為: {bmi}")
except:
    print("請輸入有效的數字")


# 比較運算子
print(1 == 1)  # True, 1等於1
print(1 != 1)  # False, 1不等於1
print(1 > 1)  # False, 1大於1
print(1 < 1)  # False, 1小於1
print(1 >= 1)  # True, 1大於等於1
print(1 <= 1)  # True, 1小於等於1

# 邏輯運算子
# and 代表全部條件都要成立才會回傳True
# or 代表只要有一個條件成立就會回傳True
# not 代表將原本的布林值反轉

print(True and True)  # True, True和True
print(True and False)  # False, True和False
print(False and False)  # False, False和False
print(True or True)  # True, True或True
print(True or False)  # True, True或False
print(False or False)  # False, False或False
print(not True)  # False, 非True
print(not False)  # True, 非False


# if
pwd = input("請輸入密碼: ")
if pwd == "123":  # 如果密碼是123
    print("密碼正確")  # 印出密碼正確

# if else
pwd = input("請輸入密碼: ")
if pwd == "123":  # 如果密碼是123
    print("密碼正確")  # 印出密碼正確
else:  # 如果密碼不是123
    print("密碼錯誤")  # 印出密碼錯誤

# if elif else
pwd = input("請輸入密碼: ")
if pwd == "123":
    print("歡迎Ray")
elif pwd == "456":  # 如果密碼是456
    print("歡迎Tom")  # 印出歡迎Tom
elif pwd == "gggggg8787878787":  # 如果密碼是456
    print("jasper")
else:
    print("密碼錯誤")

# if elif else是連續的判斷，只要有一個條件成立，後面的判斷就不會執行
# if 一定要有，elif可以有多個但是選用，else只能有一個但是選用
