A = int(input())
B = int(input())
if (A != 0 and A != 1) or (B != 0 and B != 1):
    print("輸入錯誤")
else:
    if A == 1 or B == 1:
        ans_or = 1
    else:
        ans_or = 0
    if A == 1 and B == 1:
        ans_and = 1
    else:
        ans_and = 0
    if A != B:
        ans_xor = 1
    else:
        ans_xor = 0
    print(f"OR={ans_or}")
    print(f"AND={ans_and}")
    print(f"XOR={ans_xor}")