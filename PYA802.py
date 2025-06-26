#請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的對應ASCII碼及其總和。
#ASCII碼:ord()回傳數值；chr()回傳對應文字
str1=input()
sum1=0
for i in str1:
    print("ASCII code for '%s' is %d" % (i,ord(i)))
    sum1+=ord(i)
print(sum1)