#Funkcija uzima listu i dictionary. Provjeri jesu li lista i dictionary, ako ne error. Provjeri imaju li isti broj elemenata. Provjeri jesu li svi elementi
# liste tipa integer. Vraća novi dictionary, gdje je value element iz liste na tom indexu ako se nalazi unutar [5,10] ako ne upisuje -1.
# Ispis : [8,7,1], {1:2,2:1,3:2} -> {1: 8, 2: 7, 3: -1}

lista1 = [8, 7, 1]
rjecnik1 = {1:2, 2:1, 3:2}

def provjeri(lista, rjecnik):
    if isinstance(lista, list) and isinstance(rjecnik, dict):
        if len(lista) == len(rjecnik):
            if [isinstance(x, int) for x in lista]:
                return {k+1:(v if v in range (5,10) else -1) for k,v in enumerate(lista)}

print(provjeri(lista1, rjecnik1))