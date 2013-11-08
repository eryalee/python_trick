
class TEXT():
    def __init__(self, stored = False):
        print "TEXT"


class Test():
    def __init__(self, **fields):
        print type(fields)
        for name in sorted(fields.keys()):
            print name, fields[name]

def cal(*fields):
    print type(fields)
    print fields

cal(9, 10)

Test(context=TEXT(stored=True), title=TEXT, name = 'lyx')
