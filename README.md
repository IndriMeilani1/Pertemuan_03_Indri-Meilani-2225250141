# Pertemuan 03 Seleksi Python

Nama : Indri Meilani
NIM : 2225250141
Kelas : 3A

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan
python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
Langkah-langkah keputusan program analisis persamaan kuadrat:
1. Program meminta pengguna memasukkan nilai a, b, dan c.
2. Program memeriksa nilai a.
  - Jika a = 0, maka persamaan tersebut bukan persamaan kuadrat.
  - Jika a ≠ 0, program melanjutkan proses.
3. Program menghitung diskriminan (D) dengan rumus b² - 4ac.
4. Program memeriksa nilai diskriminan menggunakan nested if:
  - Jika D > 0, persamaan mempunyai dua akar real yang berbeda.
  - Jika D = 0, persamaan mempunyai satu akar real kembar.
  - Jika D < 0, persamaan tidak mempunyai akar real.
5. Jika terdapat akar real, program menghitung dan menampilkan nilai akarnya.
6. Program selesai.

## Hasil Pengujian
asil pengujian program dengan beberapa kondisi nilai diskriminan:
1. Input a = 1, b = -5, c = 6
   - 	Keluaran yang Diharapkan Diskriminan = 1, sehingga memiliki dua akar real berbeda, yaitu 3 dan 2.	keluaran aktual Program menampilkan diskriminan 1.00, dua akar real berbeda, yaitu 3.00 dan 2.00.	status Berhasil.
2. Input a = 1, b = -4, c = 4
   - Keluaran yang Diharapkan Diskriminan = 0, sehingga memiliki satu akar real kembar, yaitu 2.	keluaran aktual Program menampilkan diskriminan 0.00 dan akar kembar 2.00.	status Berhasil.
3. Input a = 1, b = 2, c = 5
   - Keluaran yang Diharapkan Diskriminan < 0, sehingga tidak memiliki akar real.	keluaran aktual Program menampilkan diskriminan -16.00 dan keterangan tidak memiliki akar real.	status Berhasil.
4. Input a = 0, b = 2, c = 1
   - Keluaran yang Diharapkan Karena a = 0, persamaan bukan persamaan kuadrat.	keluaran aktual Program menampilkan "Bukan persamaan kuadrat."	status Berhasil.

## Refleksi
Satu kesalahan logika yang ditemukan adalah tidak memberikan kondisi ketika nilai a sama dengan 0. Jika a = 0, persamaan tersebut bukan lagi persamaan kuadrat, tetapi program tetap bisa mencoba menghitung diskriminan.
Cara memperbaikinya adalah dengan menambahkan percabangan if untuk memeriksa nilai a terlebih dahulu. Jika a == 0, program menampilkan pesan "Bukan persamaan kuadrat." dan tidak melanjutkan perhitungan. Jika a tidak sama dengan 0, barulah program menghitung diskriminan dan menentukan jenis akarnya.
