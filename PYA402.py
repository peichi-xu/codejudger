#請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值。
listA=[]
n=0
while n!=9999:
    n=eval(input())
    listA.append(n)
print(min(listA))#要熟記一下語法
