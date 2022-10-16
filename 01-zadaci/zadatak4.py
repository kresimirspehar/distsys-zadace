#Funkcija prima dvije liste, provjerava dal su istih duljina, ako nisu raise-a Error. Vraća novu listu uspoređujući elemente na istim indeksima. Ako
#su vrijednosti iste, vraća taj element, ako nisu vraća -1 na toj poziciji. (Funkcija mora imati dvije linije)
#Ispis: [1,2,3,4,5],[2,2,4,4,5] -> [-1, 2, -1, 4, 5]

lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 2, 4, 4, 5]

def provjeri(lista1, lista2):
    if len(lista1) == len(lista2):
        return [x if x == lista2[i] else -1 for i, x in enumerate(lista1)]

print(provjeri(lista1, lista2))