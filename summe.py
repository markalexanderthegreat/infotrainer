import random
def summe(a,b):   # schwierige Berechnungen in eine Funktion auslagern
    return a + b

def summe_ui():
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    print('Was ist die Summe von',a,'und',b,'?')
    input()       # weiter mit Datenfreigabe
    print('Die Summe ist',summe(a,b))
