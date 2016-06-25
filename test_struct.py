

import struct

print
print '==========pack - unpack==========='

str = struct.pack("<ii", 20, 400)
str1 = struct.pack(">ii", 20, 400)
print str
print str1
print repr(str)
print repr(str1)

print struct.calcsize("iic")
print struct.calcsize("4i")

if __name__ == '__main__':
    print 'hello'
