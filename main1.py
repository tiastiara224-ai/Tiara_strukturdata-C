#index  0(-4)     1(-3)     2(-2)     3(-1)
nama = ["tiara", "amrina", "ratian", "noer"]
dosen = ["edy", "jarir", "iman", "fuad", "indri"]

# mengambil data dari list
data_pertama = nama[-2]
print(f"data pertama : {data_pertama}")

# mengambil data terakhir
data_terahir = nama[-1]
print(f"data terahir : {data_terahir}")

# menambahkan data
# nama.insert(posisi,item)
nama.insert(1, "dika")
print(f"data setlh ditambah : {nama}")

# menambah data di paling ahir
# nama.insert(-1,"zulfikar")
nama.append("zulfikar")
print(f"data setlh ditambah diahir: {nama}")

# menggabungkan list
nama.extend(dosen)
print(f"data list gabung: {nama}")

# menggabungkan nama dosen di tengah
nama[2:2] = dosen
print(f"data list gabung dosen ditengah: \n{nama}")

# merubah data
nama[0] = "up to you"
print(f"data setelah diedit : {nama}")

# menghapus data
nama.remove("iman")
print(f"data setelah dihapus: \n{nama}")

# menghapus data paling ahir
nama.pop()
print(f"data paling ahir dihapus: \n{nama}")