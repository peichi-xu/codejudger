#請撰寫一程式，首先要求使用者輸入正整數k（1 <= k <= 100），代表有k筆測試資料。每一筆測試資料是一串數字，每個數字之間以一空白區隔，請找出此串列數字中最大值和最小值之間的差。
#提示：差值輸出到小數點後第二位。
n = eval(input())
for i in range(n):
    str1=input()
    listA = [eval(j) for j in str1.split()]#為下面兩段的精簡
    # listA=str1.split()
    # listA=[eval(i) for i in listA]#把字串轉為數值帶回list
    print('%.2f' % (max(listA)-min(listA)))#小數點位數要在這控制
    
