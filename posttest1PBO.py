class Klien:
    total_klien = 0
    def __init__(self,id, nama, no_hp):
        self.id = id
        self.nama = nama
        self.__no_hp = no_hp

        Klien.total_klien += 1

    @property
    def no_hp(self):
        return self.__no_hp
        
    @no_hp.setter
    def no_hp(self, no_hp_baru):
        if self.validasi_no_hp(no_hp_baru):
            self.__no_hp = no_hp_baru
        else:
            print("Nomor HP harus angka.")

    @staticmethod
    def validasi_no_hp(no_hp):
        return str(no_hp).isdigit()

class JasaEdit:
    total_projek = 0
    def __init__(self,kode, projek, durasi, harga):
        self.kode = kode
        self.projek = projek
        self.__durasi = durasi
        self.__harga = harga

        JasaEdit.total_projek += 1

    @property
    def durasi(self):
        return self.__durasi
    
    @durasi.setter
    def durasi(self, durasi_baru):
        if durasi_baru > 0:
            self.__durasi = durasi_baru
        else:
            print("Durasi harus lebih dari 0.")

    @property
    def harga(self):
        return self.__harga
    
    @harga.setter
    def harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
        else:
            print("Harga harus lebih dari 0.")

class Tagihan: 

    ppn = 0.11

    def __init__(self, id_tagihan, klien, jasa_edit):
        self.id_tagihan = id_tagihan
        self.klien = klien
        self.jasa_edit = jasa_edit
        self.__status = "Belum Lunas"

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status_baru):
        if status_baru in ["Belum Lunas", "Lunas"]:
            self.__status = status_baru
        else:
            print("Status harus 'Belum Lunas' atau 'Lunas'.")
            
    def total_tagihan(self):
        total = self.jasa_edit.harga * self.jasa_edit.durasi
        total_ppn = total * Tagihan.ppn
        return total + total_ppn
    
    @classmethod
    def ubah_ppn(cls, ppn_baru):
        cls.ppn = ppn_baru
        print(f"PPN berhasil diubah menjadi {cls.ppn * 100}%")

k1 = Klien("K001", "ridho", "08123456789")
k2 = Klien("K002", "jaki", "08198765432")

j1 = JasaEdit("J001", "Short Movie", 5, 100000)
j2 = JasaEdit("J002", "Tugas video", 2, 50000)

t1 = Tagihan("T001", k1, j1)
t2 = Tagihan("T002", k2, j2)

print(f"Total tagihan 1 {t1.klien.nama} adalah Rp {t1.total_tagihan()}")
print(f"Validasi nomor HP {k1.nama}: {k1.validasi_no_hp(k1.no_hp)}")
Tagihan.ubah_ppn(0.15)

print("Uji data tidak valid")
k1.no_hp = "abc"
j1.durasi = -5
t1.status = "Gatau"

print("Uji data valid")
k1.no_hp = "08123456789"
j1.durasi = 5
t1.status = "Lunas"

print(f"Status tagihan 1 baru {t1.klien.nama} adalah {t1.status}")
print(f"Total tagihan 1 baru {t1.klien.nama} adalah Rp {t1.total_tagihan()}")
