def volumtabung(r, t):
    phi = 3.14
    volume = phi * r * r * t
    print('Volume tabung:', volume, 'cm3')
r = float(input('Masukkan jari-jari tabung:'))
t = float(input('Masukkan tinggi tabung:'))
volumtabung(r, t)    