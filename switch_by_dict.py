#coding:gbk
#!/usr/bin/python
#switch implemented by using dict
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
