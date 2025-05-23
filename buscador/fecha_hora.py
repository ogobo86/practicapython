from datetime import date

#importa datetime
#mi_dia2 = datetime (2025, 5, 21, 13, 30, 12, 345)
#mi_dia2 = mi_dia2.replace(month=11)
#print (mi_dia2)

nacimiento = date (1986, 7, 31)
defuncion = date (2025, 11, 13)

vida = defuncion - nacimiento

print (vida.days)