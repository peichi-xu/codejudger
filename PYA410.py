#以 * 畫出等腰三角形（每列最後一個 * 的右方無空白）
n = eval(input())

for i in range(n):
    for j in range(n-i,1,-1):
        print(' ',end='')
    for k in range(0,i*2+1,1):
        print('*',end='')
    print()
