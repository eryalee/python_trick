
import dis

#python verision >= 2.6

def plus(number):
    def plus_in(num_in):
        y = 100
        return num_in + number
    return plus_in

v1 = plus(20)
print v1(100)

dis.dis(v1)
print v1.__closure__

#print '*' * 90
#print dir(plus)
#print plus.__closure__  #None

#another test
#v2 = plus(40)
#print v2(200)
