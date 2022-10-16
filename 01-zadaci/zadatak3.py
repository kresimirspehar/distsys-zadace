#Funkcija uzima listu dictionary-a o artiklima. Provjerava je li parametar lista, ak ne error. Provjerava jesu li svi elementi dictionary, ako ne error.
#Provjerava imaju li svi dictionary odgovarajuća 3 ključeva, ako ne error. (“cijena”,“naziv”,“kolicina”) (Moze i u dvije linije) Vraća novi nested
#dictionary s ključem “ukupno” i dictionary sa ključem “artikli” i listom svih odabranih artikala te “cijena” s ukupnom cijenom računa. (Ne treba
#biti One-liner) Ispis: [{“cijena”:8,“naziv”:“Kruh”,“kolicina”:1}, {“cijena”:13,“naziv”:“Sok”,“kolicina”:2},
#{“cijena”:7,“naziv”:“Upaljac”,“kolicina”:1}] -> {‘ukupno’: {‘artikli’:[‘Kruh’, ‘Sok’, ‘Upaljac’], ‘cijena’: 57}}

dic_list = [{"cijena":8, "naziv":"Kruh", "kolicina":1}, {"cijena":13, "naziv":"Sok", "kolicina":2}, {"cijena":7, "naziv":"Upaljac", "kolicina":1}]

def artikli(x):
    artikl = ["cijena", "naziv", "kolicina"]
    rezultat = {'ukupno': {'artikli':[], 'cijena': 0}}
    
    assert all(isinstance(i, dict)for i in x)

    assert all(list(i.keys())== artikl for i in x )

    assert isinstance(x, list)
    
    for i in x:
        rezultat['ukupno']['artikli'].append(i['naziv'])
        rezultat['ukupno']['cijena'] +=  i['kolicina'] * i['cijena']
    return rezultat

print(artikli(dic_list))

