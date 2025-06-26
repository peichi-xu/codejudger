#請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳a**b的值。
n1 = int(input())
n2 = int(input())
def compute(a,b):
    print(a**b)
    return a**b
compute(n1,n2)

# =============================================================================
# n1 = int(input())
# n2 = int(input())
# def compute(a,b):
#     result=a**b#不用在外面先賦值result，因為還是需要新變數承接
#     return result
# re2=compute(n1,n2)#即使return了result，在呼叫函式的時候還是要給他一個新的容器承接
# print(re2)
# =============================================================================
