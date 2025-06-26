#請撰寫一程式，要求使用者輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字。
listA=[]
for i in range(10):
    x=eval(input())
    listA.append(x)
listA.sort(reverse=True)#reverse=True:由大到小
print(listA[0],listA[1],listA[2])#沒打出來的地方

# =============================================================================
# 老師的寫法
# lst=[]  
# for i in range(10):
#     lst.append(eval(input()))
# lst.sort()
# print(listA[-1],listA[-2],listA[-3])
# =============================================================================
