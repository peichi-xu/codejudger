#請使用迴圈敘述撰寫一程式，要求使用者輸入一個數字，此數字代表後面測試資料的數量。每一筆測試資料是一個正整數（由使用者輸入），將此正整數的每位數全部加總起來。
#要注意的是字串才能做for in
n1=eval(input())
for i in range(n1):
    sum1=0
    x=input()
    for i in x:
        sum1+=int(i)
    print('Sum of all digits of %s is %d'%(x,sum1))



