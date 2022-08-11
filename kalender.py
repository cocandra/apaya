import calendar

# Menerima masukkan tahun dari user
tahun = int(input("Input tahun: "))
#Menerima masukkan bulan dari user
bulan = int(input("Input bulan: "))

#Cetak bulan sesuai tahun yang dimasukkan
print(calendar.month(tahun,bulan))