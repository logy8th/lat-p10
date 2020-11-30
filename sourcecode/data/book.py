data = []
data = {}

def add():
    while True:
        c  = input("(T)ambah, (U)bah, (H)apus: ")
        if c.lower() == 't':
            print("=====Tambah Data Mahasiswa=====")
            nama    =input("Nama                :  ")
            nim     =input("NIM                 :  ")
            nomortelpon =input("Nomor Telpon        :  ")
            data[nama] = nama, nim, nomortelpon
            break

        elif c.lower() == 'u':
            print('============Ubah Nomor Telpon Mahasiswa============')
            nama = input('Nama                          :  ')
            if nama in data.keys():
                nama    =input("Nama                :  ")
                nim     =input("NIM                 :  ")
                nomortelpon =input("Nomor Telpon        :  ")
                data[nama] = namdata = []
data = {}

def add():
    while True:
        c  = input("(T)ambah, (U)bah, (H)apus: ")
        if c.lower() == 't':
            print("=====Tambah Data Mahasiswa=====")
            nama    =input("Nama                :  ")
            nim     =input("NIM                 :  ")
            nomortelpon =input("Nomor Telpon        :  ")
            data[nama] = nama, nim, nomortelpon
            break

        elif c.lower() == 'u':
            print('============Ubah Nomor Telpon Mahasiswa============')
            nama = input('Nama                          :  ')
            if nama in data.keys():
                nama    =input("Nama                :  ")
                nim     =input("NIM                 :  ")
                nomortelpon =input("Nomor Telpon        :  ")
                data[nama] = nama, nim, nomortelpon

            else:
                print("Data Nilai Tidak Ada".format(nama))
                break

        elif c.lower() == 'h':
            print("====Hapus Nomor Telpon Mahasiswa====")
            nama=input("nama :  ")
            if nama in data.keys():
                del data[nama]
            else:
                print("Nomor Telpon Tidak Ada".format(nama))
                break

def show():
    print("Daftar Nomor Telepon Mahasiswa")
    print("===========================================================")
    print(" |   NO   |     NAMA      |    NIM    |     NOMOR TELPON    | ")
    print("===========================================================")
    i=0
    for x in data.values():
        i+=1
        print(" |   {0:2}   |   {1:10}  |   {2:10}  |   {3:10}  |".format(i, x[0], x[1], x[2]))
        print("===========================================================")