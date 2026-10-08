num = int(input("請輸入一個0~15的整數："))
if num < 0 or num > 15:
    print("輸入錯誤")
else:
    b3 = num // 8
    rem3 = num % 8
    b2 = rem3 // 4
    rem2 = rem3 % 4
    b1 = rem2 // 2
    b0 = rem2 % 2
    binary = f"{b3}{b2}{b1}{b0}"
    o1 = num // 8
    o0 = num % 8
    octal = f"{o1}{o0}"
    if num == 10:
        hex = "A"
    elif num == 11:
        hex = "B"
    elif num == 12:
        hex = "C"
    elif num == 13:
        hex = "D"
    elif num == 14:
        hex = "E"
    elif num == 15:
        hex = "F"
    else:
        hex = str(num)
    print(f"二進制={binary}")
    print(f"八進制={octal}")
    print(f"十六進制={hex}")