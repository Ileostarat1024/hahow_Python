def divided_by_0(func):
    def denom_test(n,d):
       try:
           return func(n,d)
       except ZeroDivisionError:
           return 0
    return denom_test

@divided_by_0
def divide(n,  d):
    return int(n) / int(d)

# n = input('請輸入分子：')
# d = input('請輸入分母：')
# print('答案為：', divide(n,d))

