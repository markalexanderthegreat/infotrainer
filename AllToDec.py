def AllToDec_ui():
    i = int(input('Ausgangsystem(z.B. Octal 8)'))
    zahl = input('Ausgangszahl:')
    input('Summe an Decimal zahlen: ')
    print(All2dec(zahl, i))


def All2dec(z, p):
    s = ''
    n = 0
    for i in range(0, len(z)):
        n += int(z[len(z) - (i + 1)], p) * (p ** i)
        s += str(int(z[len(z) - (i + 1)], p)) + '*' + str(p ** i) + ' + '
    s = s[:-3] + ' = ' + str(n)
    return s


if __name__ == '__main__':
    AllToDec_ui()