def read_data(filename):
    incr = 0
    numbered_list = []
    data = open(filename, 'r').read()
    data = data.replace('\n', ' ')
    data = list(data.split(' '))
    while incr < len(data):
        numbered_list.append(eval(data[incr]))
        incr += 1
    numbered_list.sort()
    return numbered_list


def is_in_linear(search_val, values):
    if search_val in values:
        return True
    else:
        return False