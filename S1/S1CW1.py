vat = 23
obliczonyVat = (1 + vat / 100)
CenaNettoJava = 10
CenaNettoAjax = 20

CennaBruttoJava = CenaNettoJava * obliczonyVat
CennaBruttoAjax = CenaNettoAjax * obliczonyVat

print(CennaBruttoJava)
print(CennaBruttoAjax)
