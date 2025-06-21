while True:
    d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
    print("目前水果價格")
    for name, price in d.items():
        print(f"{name}:{price}元")
