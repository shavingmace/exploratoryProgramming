def sign(num):
    answer = '?'
    if num > 0:
        answer = '+'
    elif num < 0:
        answer = '-'
    else:
        answer = ''
    return answer

print(sign(4))
print(sign(-20))
print(sign(0))
print(sign(1))
