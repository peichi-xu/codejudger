#請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。
#注意要輸出的文字，while True:搭配break
lst1=[]
lst2=[]
print('Create tuple1:')
while True:
    n=eval(input())
    if n == -9999:
        break
    else:
        lst1.append(n)
print('Create tuple2:')
while True:
    n=eval(input())
    if n == -9999:
        break
    else:
        lst2.append(n)

lst3=lst1+lst2
print('Combined tuple before sorting:',tuple(lst3))
lst3.sort()#不能在print裡面直接做
print('Combined list after sorting:',lst3)

# =============================================================================
# 示範語法
# tup1 = ()
# tup2 = ()
# print('Create tuple1:')
# while True:
#     n = eval(input())
#     if n == -9999:
#         break
#     else:
#         tup1 += (n,)
# print('Create tuple2:')
# while True:
#     n = eval(input())
#     if n == -9999:
#         break
#     else:
#         tup2 += (n,)
# 
# tup_comb = tup1+tup2
# print('Combined tuple before sorting:', tup_comb)
# lst1 = list(tup_comb)
# print('Combined list after sorting:', sorted(lst1))
# =============================================================================
