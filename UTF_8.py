def UTF8_ui():
    print('UTF-8 Masken:')
    print('     0000 -      007F: 0xxxxxxx')
    print('     0080 -      07FF: 110xxxxx 10xxxxxx')
    print('     0800 -      FFFF: 1110xxxx 10xxxxxx 10xxxxxx')
    print('0001 0000 - 0010 FFFF: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx')
    dezimal = input('Codepoint Dezimal: ')
    if int(dezimal) > int('10FFFF', 16):
        print('Dezimaler Codepoint zu groß!')
        return
    input('Codepoint Hexadezimal: ')
    print('Codepoint Hexadezimal: ' + str(hex(int(dezimal)))[2:])
    input('Codepoint Binär: ')
    binaer_str = str(bin(int(dezimal)))[2:]
    i = 4
    while i < len(binaer_str):
        binaer_str = binaer_str[:i] + ' ' + binaer_str[i:]
        i += 5
    print('Codepoint Hexadezimal: ' + binaer_str)
    input('Maske:')
    if int(dezimal) < int('007F', 16):
        print('Maske: 0xxxxxxx')
        mask = '0xxxxxxx'
    elif int(dezimal) < int('07FF', 16):
        print('Maske: 110xxxxx 10xxxxxx')
        mask = '110xxxxx 10xxxxxx'
    elif int(dezimal) < int('FFFF', 16):
        print('Maske: 1110xxxx 10xxxxxx 10xxxxxx')
        mask = '1110xxxx 10xxxxxx 10xxxxxx'
    elif int(dezimal) < int('10FFFF', 16):
        print('Maske: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx')
        mask = '11110xxx 10xxxxxx 10xxxxxx 10xxxxxx'
    input('Eingesetzt in Maske: ')
    binaer_str = str(bin(int(dezimal)))[2:]
    u = len(binaer_str) - 1
    mask = list(mask)
    for i in range(len(mask)-1,-1,-1):
        if mask[i] == 'x':
            if u < 0:
                mask[i] = '0'
            else:
                mask[i] = binaer_str[u]
                u -= 1
    mask = ''.join(mask)
    print('Eingesetzt in Maske: ' + mask)
    input('In 4-er Blöcke eingeteilt: ')
    i = 4
    while i < len(mask):
        mask = mask[:i] + ' ' + mask[i:]
        i += 10
    print('In 4-er Blöcke eingeteilt: ' + mask)
    input('UTF-8 Codierung: ')
    mask = mask.replace(' ', '')
    print('UTF-8 Codierung: ' + str(hex(int(mask, 2)))[2:])

if __name__ == '__main__':
    UTF8_ui()