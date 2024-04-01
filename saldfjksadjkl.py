def fnum(x1, x2, x3):
    if (999 < x1 < 10000 and 999 < x2 < 10000 and not(999 < x3 < 10000)) or (999 < x1 < 10000 and 999 < x3 < 10000 and not(999 < x2 < 10000)) or (999 < x2 < 10000 and 999 < x3 < 10000 and not(999 < x1 < 10000)):
        return True
    else:
        return False

def xo(x1, x2, x3):
    if x1 % 5 == 0 or x2 % 5 == 0 or x3 % 5 == 0:
        return True
    else:
        return False

def su(x1, x2, x3, p):
    if x1 + x2 + x3 > p:
        return True
    else:
        return False

f = open('17_13088.txt')
m = [int(x) for x in f]
ma_sem = -1
k = 0
ma = -1

for i in range(len(m)):
    if m[i] % 100 == 17 and m[i] > ma_sem:
        ma_sem = m[i]

print(ma_sem)

for i in range(len(m) - 2):
    if fnum(m[i], m[i + 1], m[i + 2]) and xo(m[i], m[i + 1], m[i + 2]) and su(m[i], m[i + 1], m[i + 2]):
        k += 1
        if m[i] + m[i + 1] + m[i + 2] > ma:
            ma = m[i] + m[i + 1] + m[i + 2]

print(k, ma)

