def fy_converter(verb):
    result = ''
    if verb[-2:] == 'fy':
        result = verb[0:-1] + 'ication'
    else:
        result = '?'
    return result

print(fy_converter('gamify'))
