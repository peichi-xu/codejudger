#請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，檢查這三個邊長是否可以組成一個三角形。若可以，則輸出該三角形之周長；否則顯示【Invalid】。
#記得if判斷可以用and or同時判斷多個條件
side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

if side1+side2>side3 and side3+side1>side2 and side3+side2>side1:
    print(side1+side2+side3)
else:
    print('Invalid')