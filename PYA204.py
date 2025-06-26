#請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。
num1=int(input())
num2=int(input())
math=input()
if math=='+':
    print(num1+num2)
elif math=='-':
    print(num1-num2)
elif math=='*':
    print(num1*num2)
elif math=='/':
    print(num1/num2)
elif math=='//':
    print(num1//num2)
elif math=='%':
    print(num1%num2)
