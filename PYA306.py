#請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。
num1=int(input())
result=1
for i in range(1,num1+1):
    result*=i
print(result)