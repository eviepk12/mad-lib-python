# Python sample for the main madlibs program
# Made by Zainal

def madlib():
    hewan = input("Hewan : ")
    negara = input("Negara : ")
    kataBendaJamak = input ("Kata Benda Jamak : ")
    makanan = input("Makanan : ")
    alatElektronik = input("Alat Elektronik : ")
    kataBenda = input("Kata Benda : ")
    kataKerja = input("Kata Kerja : ")
    kataSifat = input("Kata Sifat : ")

    print("-------------------------------------")

    madlibs = f"Sang agung  {hewan} sudah mengembara {negara} \
selama ribuan tahun. Sekarang, dia mengembara untuk mencari {kataBendaJamak}. \
Dia harus mencari makanan untuk bertahan hidup. Saat ia memburu {makanan}, dia menemukan sebuah \
{alatElektronik} yang tersembunyi dibalik {kataBenda}. Dia tidak pernah \
melihat sesuatu seperti itu sebelumnya. Apa yang akan dia lakukan? dengan alatnya di giginya, \
dia mencoba untuk {kataKerja}, tetapi tidak terjadi apa-apa. Dia mengambilnya kembali \
ke keluarganya. Saat keluarganya melihat, mereka dengan cepat {kataKerja} \
dengan cepat, alatnya menjadi {kataSifat}, keluarganya menentukan untuk mengembalikannya \
ke tempat yang semula."
    
    print(madlibs)