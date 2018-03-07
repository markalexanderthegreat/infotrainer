

def getBuchstabenListe(text):
    '''
    text : String mit dem zu codierenen Text
    returns: Liste mit Objekten vom Typ Buchstabe mit der
        Häufigkeit ihres Auftretens in text
    '''
    buchstaben = []
    for c in text:
        gefunden = False
        for b in buchstaben:
            if c == b.zeichen:
                b.addOne()
                gefunden = True
        if not gefunden:
            buchstaben.append(Buchstabe(c, 1))
    return buchstaben
    
def getNaechste(buchstaben):
    '''
    buchstaben: Liste mit Buchstaben-Objekten
    returns: (b1,b2) Tupel mit den beiden Buchstaben-Objekten in
        der Liste buchstaben, die die niedrigste Zahl(nummer) haben.
    '''   
    if buchstaben[0].nummer <= buchstaben[1].nummer:
        links = buchstaben[0]
        rechts = buchstaben[1]
    else:
        links = buchstaben[1]
        rechts = buchstaben[0]
    for i in range(2,len(buchstaben)):
            c = buchstaben[i]
            if c.nummer < links.nummer:
                rechts = links
                links = c
            elif c.nummer < rechts.nummer:
                rechts = c
    return (links,rechts)
    
def merge(buchstaben):
    '''
    buchstaben: Liste mit Buchstaben-Objekten
    returns: None, merged die Buchstaben in der Liste gemäß
       dem Huffman-Algorithmus. Die Liste buchstaben hat dann nur 
       noch ein Element, den Huffman-Baum.
    '''
    while len(buchstaben) > 1:
        links, rechts = getNaechste(buchstaben)
        input()
        print('Nächster merge: {} {} zu {}'.format(links,rechts,links.nummer+rechts.nummer),end='')
        buchstaben.remove(links)
        buchstaben.remove(rechts)
        new_Branch = Branch(links, rechts)
        buchstaben.append(new_Branch)
    
def Huffman_ui():
    eingabe = input('Eingabe des zu codierenden Strings: ')
    
    buchstabenListe = getBuchstabenListe(eingabe)
    
    print('Buchstabenhäufigkeit: ',end='')
    for b in buchstabenListe:
        print(b, end=' ')
        
    buchstabenListe_kopie = buchstabenListe[:]
    merge(buchstabenListe)
    
    buchstabenListe[0].encoding('')
    buchstabenListe_kopie.sort(key = lambda x: x.code)
    
    print()
    print('Huffman-Codierung: ',end='')
    for b in buchstabenListe_kopie:
        print(b.zeichen,'=',b.code, end=' ')

class Buchstabe():
    def __init__(self, char, nummer):
        self.nummer = nummer
        self.zeichen = char
        self.code = None
        
    def addOne(self):
        self.nummer += 1
    def encoding(self, code):
        self.code = code
    def __str__(self):
        return self.zeichen + ' ' + str(self.nummer)


class Branch():
    def __init__(self, left, right):
        self.nummer = left.nummer + right.nummer
        self.left = left
        self.right = right
        self.zeichen = left.zeichen + right.zeichen
    def encoding(self, previos):
        self.left.encoding(previos + '0')
        self.right.encoding(previos + '1')
    def __str__(self):
        return self.zeichen + ' ' + str(self.nummer)

if __name__ == '__main__':
    Huffman_ui()
