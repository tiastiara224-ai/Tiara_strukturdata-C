
nama = input("masukan nama")

if nama == "tiara" :
    print("Hai tiara")
    print("silahkan lanjut ke program selanjutnya")

else : 
    print("nama anda salah")
    print("silahkan coba lagi")    

try:
    angka = input("mau lihat perkalian berapa")
    print(f"n\tabel perkalian {angka}")

#menggunakan range(1,11) untuk perkalian 1 sampai 11
 for i in range(1, 11) :
    hasil = angka*i
    print(f"{angka} * {i} = angka*i")
