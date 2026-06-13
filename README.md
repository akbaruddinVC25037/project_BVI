iskandar
zaki
akbar

🟢 SISTEM PENGURUSAN PERBELANJAAN PERIBADI (PENJELASAN DETAIL)

Sistem ini ialah aplikasi desktop yang dibangunkan menggunakan Python dengan pustaka Tkinter sebagai antaramuka pengguna. Tujuan utama sistem ini adalah untuk membantu pengguna merekod, mengurus dan menganalisis perbelanjaan harian mereka secara lebih teratur dan sistematik.

🔐 1. SISTEM LOGIN DAN REGISTER

Apabila aplikasi dimulakan, pengguna akan melihat halaman login. Pengguna perlu mempunyai akaun untuk memasuki sistem. Jika belum mempunyai akaun, pengguna boleh mendaftar melalui fungsi “Create New Account”.

Semasa pendaftaran, pengguna perlu memasukkan username dan password. Sistem akan menyemak:

Username tidak boleh melebihi 15 aksara
Password mesti terdiri daripada nombor sahaja dan maksimum 6 digit
Username tidak boleh sama dengan pengguna lain

Semua maklumat pengguna akan disimpan dalam fail users.csv. Selepas berjaya log masuk, sistem akan menetapkan pengguna sebagai logged_user dan membuka dashboard utama. Setiap pengguna akan mempunyai fail CSV sendiri untuk menyimpan data perbelanjaan.

🏠 2. DASHBOARD UTAMA

Selepas log masuk, pengguna akan masuk ke dashboard utama yang mengandungi dua bahagian utama iaitu panel kiri dan panel kanan.

🟦 3. PANEL KIRI (INPUT DATA & STATUS)

Panel kiri digunakan untuk memasukkan data perbelanjaan dan melihat status kewangan.

Pengguna perlu memasukkan:

Gaji bulanan (salary)
Kategori perbelanjaan (contoh: Food, Transport, Bills, Shopping)
Tarikh menggunakan calendar
Jumlah perbelanjaan (RM dan sen)
Penerangan atau nota perbelanjaan

Selepas data dimasukkan, pengguna boleh menekan butang ADD untuk menyimpan data ke dalam sistem.

Selain itu, terdapat juga:

Butang UNDO untuk membatalkan tindakan terakhir
Butang CLEAR untuk memadam semua data
Paparan status kewangan yang menunjukkan keadaan kewangan pengguna seperti “HEALTHY”, “HIGH SPENDING” atau “OVERSPENDING” berdasarkan perbandingan gaji dan jumlah perbelanjaan
🟨 4. PANEL KANAN (JADUAL & ANALISIS)

Panel kanan memaparkan semua data perbelanjaan dalam bentuk jadual (Treeview). Jadual ini mengandungi:

Tarikh
Hari
Kategori
Jumlah
Penerangan

Data akan disusun mengikut tarikh secara automatik untuk memudahkan pengguna melihat urutan perbelanjaan.

🔍 5. FUNGSI CARIAN DAN FILTER

Sistem menyediakan fungsi carian untuk menapis data berdasarkan:

Kata kunci (keyword)
Kategori
Tarikh (optional filter menggunakan calendar)

Pengguna juga boleh menekan butang “VIEW ALL” untuk memaparkan semua data semula tanpa penapis.

💰 6. PENGIRAAN JUMLAH PERBELANJAAN

Sistem akan mengira jumlah keseluruhan perbelanjaan secara automatik berdasarkan semua data dalam jadual. Jumlah ini akan dipaparkan di bawah jadual sebagai “Total Spending”.

Selain itu, sistem juga mengira baki kewangan pengguna dengan formula:

Baki = Gaji bulanan - Jumlah perbelanjaan

Berdasarkan nilai ini, sistem akan menentukan status kewangan pengguna.

📊 7. ANALISIS GRAF (CHART)

Sistem juga menyediakan fungsi grafik menggunakan matplotlib. Data perbelanjaan akan dipaparkan dalam bentuk pie chart untuk menunjukkan peratusan perbelanjaan mengikut kategori seperti Food, Transport, Bills dan lain-lain.

📄 8. GENERATE LAPORAN PDF

Sistem boleh menghasilkan laporan dalam bentuk PDF menggunakan ReportLab. Laporan ini mengandungi:

Tajuk laporan
Nama pengguna
Tarikh penjanaan laporan
Jadual perbelanjaan
Jumlah keseluruhan perbelanjaan

Jika data terlalu banyak, sistem akan automatik membuat halaman baru.

📊 9. GENERATE LAPORAN EXCEL

Selain PDF, sistem juga boleh menjana laporan Excel menggunakan openpyxl. Fail Excel ini mengandungi:

Tajuk laporan berwarna
Header jadual
Data perbelanjaan
Format selang-seli (zebra style)
Jumlah keseluruhan (TOTAL SPENDING)

Fail ini disimpan sebagai:
username_report.xlsx

🔄 10. FUNGSI TAMBAHAN

Sistem juga menyediakan beberapa fungsi tambahan seperti:

Undo untuk kembali ke data sebelumnya
Delete untuk memadam data terpilih
Clear untuk memadam semua data
Auto save ke dalam CSV
Backup data sementara sebelum perubahan dibuat
📌 11. STRUKTUR PENYIMPANAN DATA

Semua data disimpan dalam format CSV dengan struktur berikut:

Username
Tarikh
Hari
Kategori
Jumlah
Penerangan

Setiap pengguna mempunyai fail berasingan untuk memastikan data tidak bercampur.

🧠 12. KESIMPULAN

Secara keseluruhan, sistem ini membantu pengguna mengurus kewangan harian dengan lebih mudah, tersusun dan sistematik. Ia bukan sahaja menyimpan data perbelanjaan, tetapi juga menyediakan analisis, laporan dan visualisasi data untuk membantu pengguna memahami corak perbelanjaan mereka.