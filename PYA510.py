#請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。
n = eval(input())

def compute(x):
 nlst = []
 for i in range(n):
    if i == 0:
        num = 0
    elif i == 1:
        num = 1
    else:
        num = nlst[i-2]+nlst[i-1]
    nlst.append(num)
    print(num, end=' ')

compute(n)
