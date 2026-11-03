def luasptabung(r, t):
    phi = 3.14
    luas = 2 * phi * r * (r + t)
    print('Luas permukaan tabung:', luas, 'cm2')
r = float(input('Masukkan jari-jari tabung'))
t = float(input('Masukkan tinggi tabung:'))
luasptabung(r, t)