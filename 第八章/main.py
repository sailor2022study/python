import computer

print(computer.add(3,5))

import computer as cp

print(cp.add(4.5))

from computer import add,sub
#引用单个或多个函数
print(add(7,9))

from computer import *
print(add(4,8))
