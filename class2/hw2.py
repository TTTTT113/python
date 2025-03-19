"""
請問Python有哪四種形態:
答案:int, float, str, bool

請問使用什麼指令可以顯示出形態
答案:type()

請問今天學了哪一些指令(函式)?
答案:max, len, type,int, float, str, bool,print,input,


延續上題, 請嘗試描述每個指令的功能各別是什麼?
答案:max(1, 2, 3, 4, 5)取最大值
len("hello")取長度
type(1)取型態
type("hello")取型態
print:用於顯示輸出到控制台
input:用於輸入輸入到控制台
type:用於顯示變數的資料型態
int:用於將資料轉換成整數
float:用於將資料轉換成浮點數型態
str:用於將資料轉換成字串型態
bool:用於將資料轉換成布林型態

"""

"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
bmi = w/h**2
EX:
請輸入身高:1.45
請輸入體重:32
你的BMI為17.301038062283737
"""
h = float(input("請輸入身高:"))
w = float(input("請輸入體重:"))
bmi = w / h**2
print("你的BMI為", bmi)
