#将八进制转化成十六进制计算器
import numpy as np
import numbers
# a = 36
# #输入待翻译的八进制数
# i =0
# while{i < a}
#     i++1

# 整数版
from functools import reduce

n = [int(x) for x in input('输入一个整数：')]
answer = reduce(lambda x, y: x * 8 + y, n)
print("the number of the n is:",answer)
#judge
# print(oct(answer))
# # a = 0o36
# if (oct(answer) == oct(0o36)):
#     print("all right")
# else:
#     print("something wrong with the program")
# # 浮点数版
# 感谢分享： http://www.codesc.net
# s = input('输入一个数，可以是浮点数：')
# try:
#     float(s)
# except ValueError:
#     print('输入错误')
# else:
#     f = s.index('.')
#     s = s[:f] + s[f + 1:]
#     s = [int(x) for x in s]
#     n = sum([8 ** (f - 1 - i) * s[i] if i < f else 8 ** (i - 1 - f) * s[i] for i in range(len(s))])
#     print(n)
final = hex(answer)
print("the final hex mode is:",final)

#原程序
# if __name__ == '__main__':
#     n = 0
#     p = raw_input('input a octal number:\n')
#     for i in range(len(p)):
#         n = n * 8 + ord(p[i]) - ord('0')
#     print(n)


