# Posttest 1 — Sistem Manajemen Order & Tarif Jasa Edit Video Creator

## Deskripsi
aku membuat Program sederhana berbasis OOP dengan menggunakan bahasa Python untuk mengelola order jasa edit video, mulai dari data klien, data editing dan perhitungan tagihannya. Program ini terdiri dari 3 class yang saling terhubung yaitu 'Klien', 'JasaEdit' dan 'Tagihan'. Class tagihan itu memakai objek dari Klien dan JasaEdit untuk menghitung total tagihan, karena itu 3 class ini saling terhubung.

## Struktur Class

### 1. "Klien"
-Atribut kelas: Total_klien(ku defult 0, jadi awalanya kosong terus nanti saat objek 'klien' baru di buat nilai nya akan ototmatis bertambah dengan cara '+=1'.)

-Atribut Public: id, nama (data ini ku buat public karena data ini memang boleh di akses lansung dari luar class)

-Atribut Private: __no_hp (data ini ku buat private karena data ini perlu dijaga supaya tidak bisa di ubah sembarangan dari luar class )

-Getter & Setter: aku buat pakai '@property' dan '@no_hp.setter' buat akses __no_hp dari luar class. Di bagian setter nya aku kasih validasi, jadi no hp baru cuma bisa keisi kalau isinya angka semua, kalau bukan angka bakal muncul pesan peringatan dan nilai lama nya tetap dipakai (ga jadi diubah).

-Static method: 'validasi_no_hp()' aku buat buat ngecek format no hp nya, apakah isinya angka semua atau bukan. Aku jadiin staticmethod karena fungsi ini cuma butuh input teksnya aja, ga butuh data dari self atau cls.

### 2. "JasaEdit"
di class JasaEdit ini aku nyimpen data satu pesanan editing video, kayak judul projeknya, durasi video, sama harga jasanya.

-Atribut kelas: total_projek (sama kayak total_klien, defaultnya 0 dan otomatis nambah tiap ada objek JasaEdit baru dibuat, buat ngitung udah berapa banyak pesanan yang masuk)

-Atribut Public: kode, projek (dua data ini boleh diakses langsung dari luar class)

-Atribut Private: __durasi, __harga (aku buat private karena dua data ini yang nentuin besar kecilnya tagihan, jadi perlu dijaga lewat validasi biar ga sembarangan diisi)

-Getter & Setter: durasi sama harga masing-masing punya getter & setter sendiri. Di setternya aku kasih validasi, nilainya cuma diterima kalau lebih besar dari 0, kalau diisi 0 atau minus bakal ditolak dan muncul pesan peringatan.

### 3. "Tagihan"
di class Tagihan ini aku gabungin objek Klien sama objek JasaEdit buat bikin satu tagihan.
-Atribut kelas: ppn (nilainya sama buat semua tagihan, bukan cuma satu objek doang, makanya aku jadiin atribut kelas)

-Atribut Public: id_tagihan, klien, jasa_edit (khusus klien sama jasa_edit, isinya bukan angka atau teks biasa, tapi objek dari class Klien dan JasaEdit, di sini nih bentuk keterhubungan antar class nya)

-Atribut Private: __status (status pembayarannya aku buat private, getter & setternya cuma nerima nilai "Belum Lunas" atau "Lunas" aja, kalau diisi teks lain bakal ditolak)

-Instance method: 'total_tagihan()' isinya ngitung harga jasa dikali durasi, terus ditambah PPN nya

-Class method: 'ubah_ppn()' (pakai 'cls') buat ngubah nilai PPN sekaligus ke semua tagihan yang ada, bukan cuma satu objek aja.

## Cara Menjalankan & Panduan Pengujian
 
1. Jalankan program dengan perintah:
```bash
   python3 posttest1PBO.py
```
2. Cek baris `Total tagihan 1 ridho = Rp 555000.0` -> bukti instance method `total_tagihan()` jalan.
3. Cek baris `Validasi nomor HP ridho = True` -> bukti staticmethod `validasi_no_hp()` jalan.
4. Cek baris `PPN berhasil diubah menjadi 15.0%` -> bukti classmethod `ubah_ppn()` berhasil mengubah atribut kelas `ppn`.
5. Di bagian "Uji data tidak valid", pastikan muncul 3 pesan peringatan (`Nomor HP harus angka.`, `Durasi harus lebih dari 0.`, `Status harus 'Belum Lunas' atau 'Lunas'.`) -> bukti validasi di setter berjalan dan menolak data yang salah.
6. Di bagian "Uji data valid", pastikan tidak ada pesan peringatan yang muncul, lalu cek baris terakhir `Status tagihan 1 baru ridho = Lunas` dan `Total tagihan 1 baru ridho = Rp 575000.0` -> bukti data berhasil diubah setelah diisi dengan nilai yang valid.
