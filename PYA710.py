# 請撰寫一程式，為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），再輸入一鍵值並檢視此鍵值是否存在於該詞典中。
dietA = {}
while True:
    # Key: (後方有一空白格)
    key = input("Key: ")
    if key == 'end':
        break
    # Value: (後方有一空白格)
    value = input("Value: ")
    dietA[key] = value  # 將key與value加入dietA中

s = input('Search key: ')
print(s in dietA)
