# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!
szam = int(input('adj meg egy számot. '))
szamm = int(input('adj meg még egy számot. '))
szammm = int(input('adj meg még egy számot. '))

if szam < szamm < szammm:
  print('az első szám a legkissebb')
elif szam > szamm > szammm:
  print('a harmadik szám a legkissebb')
else:
  print('a második a legkissebb')