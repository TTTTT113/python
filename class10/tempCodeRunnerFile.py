weather_list = [
    "晴",
    "多雲",
    "陰雨",
    "陽光",
    "雷雨",
    "雨",
    "暴雨",
]

print(weather_list)

while True:

    try:
        ans = int(input("請輸入要修改的星期數字(1-7):"))
    except:
        print("請輸入數字編號")
    else:

        if ans > len(weather_list) or ans < 1:
            print("輸入錯誤查無此星期,請重新輸入")

        else:

            print("您要修改的星期是" + str(ans))
            print("原本的天氣是" + weather_list[ans - 1])
            new_weather = input("請輸入新的天氣:")
            weather_list[ans - 1] = new_weather
            print("修改後的天氣是" + weather_list[ans - 1])
            print((weather_list))
            break
