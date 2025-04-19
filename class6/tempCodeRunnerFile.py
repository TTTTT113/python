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
