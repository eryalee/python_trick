


#closure application
#1.configuration
def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        file_doc = [i for i in lines if keep in i]
        return file_doc
    return the_filter


filter = make_filter("pass")
filter_res = filter("sample")
print filter_res


def make_file(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    def filter(keep):
        print lines
        file_doc = [i for i in lines if keep in i]
        return file_doc
    return filter

print '*' * 90
first = make_file("sample")
first_res = first("ni")
print first_res

#2. game radix
origin = [0, 0]
def create(pos = origin):
    def player(direction, step):
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step
        pos[0] = new_x
        pos[1] = new_y
        return pos
    return player

player = create()
print player([1, 0], 10)
print player([0, 1], 20)
print player([-1, 0], 10)




