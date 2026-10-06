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

    def bayar_tagihan(self, tagihan):
        if tagihan.klien != self:
            print(f"{self.nama} tidak dapat membayar tagihan milik {tagihan.klien.nama}.")
            return
        elif tagihan.status == "Lunas":
            print(f"Tagihan {tagihan.id_tagihan} sudah lunas.")
        else:
            print(f"{self.nama} membayar tagihan {tagihan.id_tagihan} sebesar Rp {tagihan.total_tagihan()}.")
            tagihan.status = "Lunas"
            tagihan.buat_catatan(tagihan.total_tagihan(), "Pembayaran lunas")

class JasaEdit:

    total_projek = 0

    def __init__(self,kode, projek, durasi, harga):
        self.kode = kode
        self.projek = projek
        self._durasi = durasi
        self._harga = harga
        self.__biaya_admin = 5000

        JasaEdit.total_projek += 1

    @property
    def durasi(self):
        return self._durasi

    @durasi.setter
    def durasi(self, durasi_baru):
        if durasi_baru > 0:
            self._durasi = durasi_baru
        else:
            print("Durasi harus lebih dari 0.")

    @property
    def harga(self):
        return self._harga
    
    @harga.setter
    def harga(self, harga_baru):
        if harga_baru > 0:
            self._harga = harga_baru
        else:
            print("Harga harus lebih dari 0.")

    def hitung_biaya(self):
        return self.__biaya_admin + (self._harga * self._durasi)

class JasaVideo(JasaEdit):
    def __init__(self, kode, projek, durasi, harga, resolusi):
        super().__init__(kode, projek, durasi, harga)
        self.resolusi = resolusi
    
    def hitung_biaya(self):
        biaya = super().hitung_biaya()
        if self.resolusi == "4K":
            biaya = int(biaya * 1.2)
        if self._durasi > 10:
            biaya += 1000
        return biaya
    
class JasaFoto(JasaEdit):
    def __init__(self, kode, projek, durasi, harga, format_foto):
        super().__init__(kode, projek, durasi, harga)
        self.format_foto = format_foto

    def hitung_biaya(self):
        biaya = super().hitung_biaya()
        if self.format_foto == "RAW":
            biaya += 20000
        return biaya
    
class Studio:
    def __init__(self, nama):
        self.nama = nama 
        self.daftar_klien = []
        self.daftar_jasa_edit = []

    def tambah_klien(self, klien):
        self.daftar_klien.append(klien)

    def tambah_jasa_edit(self, jasa_edit):
        self.daftar_jasa_edit.append(jasa_edit)

class CatatanPembayaran:
    def __init__(self, id_catatan, nominal, keterangan):
        self.id_catatan = id_catatan
        self.nominal = nominal
        self.keterangan = keterangan

class Tagihan: 

    ppn = 0.11

    def __init__(self, id_tagihan, klien, jasa_edit):
        self.id_tagihan = id_tagihan
        self.klien = klien
        self.jasa_edit = jasa_edit
        self.__status = "Belum Lunas"
        self._riwayat = []

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
        total = self.jasa_edit.hitung_biaya()
        total_ppn = total * Tagihan.ppn
        return int(total + total_ppn)

    @classmethod
    def ubah_ppn(cls, ppn_baru):
        cls.ppn = ppn_baru
        print(f"PPN berhasil diubah menjadi {cls.ppn * 100}%")

    def buat_catatan(self, nominal, keterangan):
        id_catatan = len(self._riwayat) + 1
        catatan = CatatanPembayaran(id_catatan, nominal, keterangan)
        self._riwayat.append(catatan)

    def tampilkan_riwayat(self):
        print(f"Riwayat pembayaran {self.id_tagihan}:")
        for c in self._riwayat:
            print(f"  - {c.id_catatan}: Rp {c.nominal} | {c.keterangan}")

S1 = Studio("Studio Edit")

k1 = Klien("K001", "ridho", "08123456789")
k2 = Klien("K002", "jaki", "08198765432")

j1 = JasaVideo("J001", "Short Movie", 5, 10000, "4K")
j2 = JasaFoto("J002", "Edit foto tugas", 2, 50000, "RAW")

t1 = Tagihan("T001", k1, j1)
t2 = Tagihan("T002", k2, j2)

S1.tambah_klien(k1)
S1.tambah_jasa_edit(j1)

k1.bayar_tagihan(t1)
k1.bayar_tagihan(t2)
k1.bayar_tagihan(t1) 
t1.tampilkan_riwayat()

print(f"Total tagihan 1 {t1.klien.nama} = Rp {t1.total_tagihan()}")
print(f"Validasi nomor HP {k1.nama} = {k1.validasi_no_hp(k1.no_hp)}")
Tagihan.ubah_ppn(0.15)

print("Uji data tidak valid")
k1.no_hp = "abc"
j1.durasi = -5
t1.status = "Gatau"

print("Uji data valid")
k1.no_hp = "08123456789"
j1.durasi = 5
t1.status = "Lunas"

print(f"Status tagihan 1 baru {t1.klien.nama} = {t1.status}")
print(f"Total tagihan 1 baru {t1.klien.nama} = Rp {t1.total_tagihan()}")

print (f"Daftar Klien di {S1.nama} = {[klien.nama for klien in S1.daftar_klien]}")

del S1
print (f"nama = {k1.nama}, projek = {j1.projek}")

del t1