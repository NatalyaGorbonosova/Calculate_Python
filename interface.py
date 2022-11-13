
# 2 + 8*3
# (2+3i) - (1-i)
def init():
    f = input('Введите выражение для вычисления: ')
    f = f.replace(' ', '')
    if 'i' in f: work = 'com'
    else: work = 'rat'
    return work
