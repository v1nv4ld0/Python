nim = []
nama = []
kelas = []

pilihan = 1
while pilihan != 0:
    print("1. masukan data.")
    print("2. tampilkan data.")
    print("3. hapus data.")
    print("0. exit.")

    pilihan = int(input("masukan pilihan anda : "))
    print('')
    print('')
    print('')
    if pilihan == 1:
        masnim = input("masukan nim : ")
        nim.append({'nim': masnim})
        masnama = input("masukan nama : ")
        nama.append({'nama': masnama})
        masakelas = input("masukan kelas : ")
        kelas.append({'kelas': masakelas})

    elif pilihan == 2:
        penentu = True
        for i in range(len(nim)):
            if penentu:
                print("nim\tnama\tkelas")
            print(nim[i]['nim'], '\t', nama[i]
                  ['nama'], '\t', kelas[i]['kelas'])
            penentu = False

    elif pilihan == 3:
        masnim = input("masukan nim : ")
        for i in range(len(nim)):
            if masnim == nim[i]['nim']:
                print(i)
                del nim[i]
                del nama[i]
                del kelas[i]
                break
    print('')
    print('')
    print('')
