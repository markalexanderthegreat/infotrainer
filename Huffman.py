import operator
def Huffman_ui():
    string = input('Eingabe des zu codierenden Strings: ')
    buchstaben = []
    for i in string:
        if i.isalpha():
            tempbool = False
            for u in buchstaben:
                if i.lower() == u.zeichen:
                    u.addOne()
                    tempbool = True
            if not tempbool:
                buchstaben.append(Buchstabe(i.lower(), 1))
    richtig_bshk = ''
    for i in buchstaben:
        richtig_bshk += i.string
        richtig_bshk += ', '
    richtig_bshk = richtig_bshk[:-2]
    bshk = input('Buchstabenhäufigkeiten:\n')
    #if not bshk == richtig_bshk:
    #    print('Falsche Eingabe!')
    #    print('Erwartet wäre:')
    print(richtig_bshk)
    #else:
    #    print('Richtig')
    print()
    print('Beichspiele:')
    print('Nächster merge: a, b mit 2')
    print('Nächster merge: ab, c mit 4', end='\n\n')
    buchstaben_raw = buchstaben[:]
    while len(buchstaben) > 1:
        next_merge = input('Nächster merge: ')
        if buchstaben[0].nummer <= buchstaben[1].nummer:
            links = buchstaben[0]
            rechts = buchstaben[1]
        else:
            links = buchstaben[1]
            rechts = buchstaben[0]
        for i in buchstaben:
            if not(i == links or i == rechts):
                if i.nummer < links.nummer:
                    rechts = links
                    links = i
                elif i.nummer < rechts.nummer:
                    rechts = i
        buchstaben.remove(links)
        buchstaben.remove(rechts)
        new_Branch = Branch(links, rechts)
        buchstaben.append(new_Branch)
        richtig_next_merge = links.zeichen + ', ' + rechts.zeichen + ' mit ' + str(links.nummer+rechts.nummer)
        #if not richtig_next_merge == next_merge:
        #    print('Falsche Eingabe')
        #    print('Erwartet:')
        print(richtig_next_merge)
        #else:
        #    print('Richtig')
    buchstaben[0].encoding('')
    buchstaben_raw.sort(key=operator.attrgetter('code'))
    right_encodings = ''
    for each in buchstaben_raw:
        right_encodings += each.zeichen + ' = ' + each.code + ', '
    right_encodings = right_encodings[:-2]
    encodings = input('Codierungen:(links nach rechts)\n')
    #if not encodings == right_encodings:
    #    print('Falsche Eingabe!')
    #    print('Erwartet:')
    print(right_encodings)
    #else:
    #    print('Richtig')
    richtig_binaer = ''
    for i in string:
        if i.isalpha():
            for u in buchstaben_raw:
                if i.lower() == u.zeichen:
                    richtig_binaer += u.code
    binaer = input('Verschlüsseltes Wort?\n')
    #if not binaer == richtig_binaer:
    #    print('Falsche Eingabe!')
    #    print('Erwartet:')
    print(richtig_binaer)
    #else:
    #    print('Richtig')

class Buchstabe():
    def __init__(self, char, nummer):
        self.nummer = nummer
        self.zeichen = char
        self.code = None
        self.string = self.zeichen + ' ' + str(self.nummer)
    def addOne(self):
        self.nummer += 1
        self.string = self.zeichen + ' ' + str(self.nummer)
    def encoding(self, code):
        self.code = code

class Branch():
    def __init__(self, left, right):
        self.nummer = left.nummer + right.nummer
        self.left = left
        self.right = right
        self.zeichen = left.zeichen + right.zeichen
    def encoding(self, previos):
        self.left.encoding(previos + '0')
        self.right.encoding(previos + '1')

if __name__ == '__main__':
    Huffman_ui()