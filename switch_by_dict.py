#coding:gbk
#!/usr/bin/python
#使用dict实现switch
from __future__ import division

x = 2
y = 3

operator = {
    '+' : x + y,
    '-' : x - y,
    '*' : x * y,
    '/' : x / y
}

print operator['/']
print operator['*']
operator1 = {
    '+' : lambda key, value:key + value,
    '-' : x - y,
    '*' : x * y,
    '/' : x / y
}
