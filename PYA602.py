#請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。
#提示：J、Q、K以及A分別代表11、12、13以及1。
num = 0
for i in range(5):
    n = input()
    if n == 'J':
        n = 11
    elif n == 'Q':
        n = 12
    elif n == 'K':
        n = 13
    elif n == 'A':
        n = 1

    num += int(n)
print(num)
