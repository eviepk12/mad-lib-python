# Python sample for the main madlibs program
# Made by Zainal

def madlib():
    kataBenda = input("Kata Benda : ")
    kataBendaJamak = input("kata Benda Jamak : ")
    kataKerja = input("Kata Kerja : ")
    bagianTubuhJamak = input("Bagian Tubuh Jamak : ")
    kataSifat = input("Kata Sifat : ")
    kataBendaJamak = input("Kata Benda Jamak : ")

    print("-------------------------------------------")

    madlibs = f"Sekarang, setiap pelajar mempunyai komputer yang cukup kecil untuk muat ke \
{kataBenda} mereka. Ia bisa memecahkan semua masalah matematika hanya dengan memencet {kataBendaJamak}. Komputer \
bisa menambah, mengkali, membagi, dan {kataKerja}. Mereka \
juga bisa {kataKerja} lebih baik dari manusia. Beberapa komputer \
adalah {bagianTubuhJamak}. Yang lain mempunyai {kataSifat} layar yang menunjukan segala macam {kataBendaJamak} \
dan {kataSifat}"

    print(madlibs)