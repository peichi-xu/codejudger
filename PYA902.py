#請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。檔案讀取完成後要關閉。
f=open('read.txt')
data2=f.read()
f.close()
# with open(r'C:\Users\ASUS\Downloads\read.txt') as file:
#     data2=file.read()
num1=data2.split()
sum=0
for i in num1:
    sum+=int(i)
print(sum)