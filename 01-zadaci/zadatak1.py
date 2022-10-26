#Funkcija uzima listu string-ova. Provjeri dal su sve stringovi, ako ne error. #Vraća novu listu, gdje su string-ovi duži od 4 znaka. (Funkcija od dvije
#linije) #Ispis: [“Pas”, “Macka”, “Stol”] -> [“Macka”]

lista1 = ['Pas', 'Macka', 'Stol']

def provjera(x):
   if isinstance(x, list):
    return [i for i in x if len(i) > 4]

print(provjera(lista1))
