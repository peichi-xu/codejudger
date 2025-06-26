#請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。
f_name = input()
str_old = input()
str_new = input()

file=open(f_name)
print("=== Before the replacement")
data=file.read()#這是txt，csv步驟稍微不太一樣
print(data)

print("=== After the replacement")
data1=data.replace(str_old, str_new)
print(data1)
file.close()
